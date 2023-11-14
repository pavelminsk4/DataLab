<template>
  <div :style="`--expert-input-width: ${width};`">
    <div v-if="label" class="label">{{ label }}</div>
    <div class="expert-field-container">
      <div v-if="hasLineNumbering" class="line-numbering"></div>

      <div
        contenteditable="true"
        ref="content"
        :class="['expert-input', 'scroll', isFocus && 'is-focus']"
        @focus="isFocus = true"
        @blur="isFocus = false"
        @keydown="customKeyPress"
        @input="keyUpHandler($event)"
      >
        <p></p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ExpertField',
  props: {
    modelValue: {type: Array, default: () => ['']},
    label: {type: String, default: ''},
    width: {type: Number, default: 320},
    hasLineNumbering: {type: Boolean, default: false},
  },
  emits: ['update:modelValue'],
  data() {
    return {
      isFocus: false,
      newValue: {
        rows: [],
        values: [],
      },
      currentSelection: 0,
      isNeedUpdateElementId: true,
      customRange: null,
    }
  },
  computed: {
    value: {
      get() {
        const queryData = {
          rows: this.getRowsFromValues(this.modelValue) || [],
          values: this.modelValue || [],
        }

        return queryData
      },
      set(val) {
        const rows = val.match(/<p\s(.*?)<\/p>/g)
        const values = rows.map((row) => this.getValueFromRow(row))

        let matchValue = [...rows]

        if (this.isNeedUpdateElementId) {
          matchValue = this.getRowsFromValues(values)
          // this.isNeedUpdateElementId = false
        }

        this.$refs.content.innerHTML = matchValue.join('')
        this.$emit('update:modelValue', values)
      },
    },
  },
  mounted() {
    this.$refs.content.innerHTML = this.value.rows.join('')
  },
  methods: {
    getValueFromRow(row) {
      return row.replace(/(<([^>]+)>)/gi, '')
    },
    getRowsFromValues(values) {
      return values.map(
        (value, index) =>
          `<p id="row-${index + 1}">${this.replaceLogicalOperators(value)}</p>`
      )
    },

    getCurrentRowElement(element) {
      if (element.localName === 'p') return element
      return this.getCurrentRowElement(element.parentElement)
    },
    getCurrentRowId() {
      const currentElement = this.getCurrentRowElement(
        window.getSelection().focusNode
      )

      const currentRowId = currentElement.id
      const currentRowNumber = +currentRowId.match(/\d+/)[0]
      // const childElementCount = element.childElementCount
      // this.isNeedUpdateElementId = currentRowNumber < childElementCount

      return currentRowNumber
    },
    spliceRows(startIndex, deleteCount, addElement) {
      const rows = [...this.value.rows]
      rows.splice(startIndex, deleteCount, addElement)
      this.value = rows.join('')
    },

    customKeyPress(event) {
      const rowNumber = this.getCurrentRowId(event.target)

      if (event.keyCode === 13) {
        if (rowNumber === this.value.rows.length) {
          event.preventDefault()
          this.spliceRows(rowNumber, 0, `<p id="row-${rowNumber + 1}"></p>`)
          this.restoreSelection(event.target, `row-${rowNumber + 1}`, 0)
          return
        }

        this.customRange = {range: 0, currentRowId: `row-${rowNumber + 1}`}
      }

      const rowLength = event.target.querySelector(`#row-${rowNumber}`)
        .innerText.length

      if (event.keyCode === 8 && rowLength <= 1 && rowNumber > 1) {
        event.preventDefault()

        this.spliceRows(rowNumber - 1, 1)

        const prevRowLength = event.target.querySelector(
          `#row-${rowNumber - 1}`
        ).innerText.length

        this.restoreSelection(
          event.target,
          `row-${rowNumber - 1}`,
          prevRowLength
        )
        return
      }

      if (event.keyCode === 46) {
        const endOffset = window.getSelection().getRangeAt(0).endOffset
        const nextRowLength = event.target.querySelector(
          `#row-${rowNumber + 1}`
        )?.innerText.length

        if (nextRowLength == null && endOffset === rowLength) {
          event.preventDefault()
          return
        }

        if (endOffset === rowLength && !nextRowLength) {
          event.preventDefault()

          const {range, currentRowId} = this.saveSelection()
          this.spliceRows(rowNumber, 1)
          this.restoreSelection(event.target, currentRowId, range)

          return
        }
      }
    },

    walk(node, func) {
      var stop = func(node)
      var children = node.childNodes
      for (var i = 0; !stop && i < children.length; i++)
        if (this.walk(children[i], func)) return true
      return stop
    },

    saveSelection() {
      const selection = window.getSelection()
      const currentRowElement = this.getCurrentRowElement(selection.focusNode)
      const currentRowId = currentRowElement.id
      const currentRange = selection.getRangeAt(0)

      if (!currentRange) return 0

      let range = 0
      this.walk(
        currentRowElement,
        (elm) => {
          if (elm.nodeType === Node.TEXT_NODE) {
            if (elm !== currentRange.endContainer) {
              range += elm.textContent.length
            } else {
              range += currentRange.endOffset
              return true
            }
          }
          return false
        },
        0
      )
      return {range, currentRowId}
    },

    findChildWithCharIndex(target, savedRowId, charIndex) {
      const currentRow = target.querySelector(`#${savedRowId}`)

      let child = currentRow.firstChild || currentRow
      let charCount = 0
      this.walk(currentRow, (elm) => {
        if (elm.nodeType === Node.TEXT_NODE) {
          const currentIndex = charCount + elm.textContent.length
          if (currentIndex < charIndex) {
            charCount += elm.textContent.length
          } else {
            child = elm
            return true
          }
        }
        return false
      })

      return {
        child,
        offsetInChild: charIndex - charCount,
      }
    },

    restoreSelection(target, savedRowId, savedRange) {
      if (savedRange == null) return

      target.focus()
      const selection = window.getSelection()
      if (selection.rangeCount > 0) selection.removeAllRanges()

      const {child, offsetInChild} = this.findChildWithCharIndex(
        target,
        savedRowId,
        savedRange
      )

      if (child) {
        const range = document.createRange()
        range.setStart(child, offsetInChild)
        range.setEnd(child, offsetInChild)
        selection.addRange(range)
      }
    },

    replaceLogicalOperators(value) {
      let highlightedStr = value

      // this.filters.map((filter) => {
      //   const regex = new RegExp('\\b' + filter + '[:]', 'g')
      //   highlightedStr = highlightedStr.replace(
      //     regex,
      //     `<span class="expert-mode_defaultColor">${filter}:</span>`
      //   )
      // })

      return highlightedStr
        .replace(/<br>/, '')
        .replace(/\(/g, '<span class="expert-mode_defaultColor">(</span>')
        .replace(/\)/g, '<span class="expert-mode_defaultColor">)</span>')
        .replace(
          /\bOR\b/g,
          '<span class="defaultColor expert-mode_or">OR</span>'
        )
        .replace(
          /\bAND\b/g,
          '<span class="defaultColor expert-mode_and">AND</span>'
        )
        .replace(
          /\bNOT\b/g,
          '<span class="defaultColor expert-mode_not">NOT</span>'
        )
    },

    keyUpHandler(event) {
      const savedRange = this.customRange || this.saveSelection()
      const {range, currentRowId} = savedRange

      this.value = event.target.innerHTML
      this.restoreSelection(event.target, currentRowId, range)
      this.customRange = null
    },
  },
}
</script>

<style lang="scss" scoped>
.expert-field-container {
  display: flex;

  width: 100%;
  min-height: 150px;
}

.label {
  margin-bottom: 8px;

  color: var(--typography-title-color);
}

.is-focus {
  border: 1px solid var(--border-active-color);
  box-shadow: 3px 3px 0px 0px #fcedf3, -3px 3px 0px 0px #fcedf3,
    3px -3px 0px 0px #fcedf3, -3px -3px 0px 0px #fcedf3;
}
</style>

<style lang="scss">
.expert-input {
  display: flex;
  flex-direction: column;

  width: 100%;
  height: 250px;
  padding: 10px;
  gap: 4px;

  border-radius: var(--border-radius);
  border: 1px solid var(--input-border-color);
  background-color: #ffffff;
  outline: none;

  p {
    width: var(--expert-input-width);
    min-height: 20px;

    // background-color: rgb(155, 155, 155);
  }
}

.expert-mode_defaultColor {
  color: #8e00d1;
}

.expert-mode_or {
  color: var(--neutral-primary-color);
}

.expert-mode_and {
  color: var(--positive-primary-color);
}

.expert-mode_not {
  color: var(--negative-primary-color);
}
</style>
