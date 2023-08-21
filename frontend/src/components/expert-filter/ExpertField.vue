<template>
  <div :style="`--expert-input-width: ${width};`">
    <div v-if="label" class="label">{{ label }}</div>
    <div class="expert-field-container">
      <div v-if="hasLineNumbering" class="line-numbering"></div>

      <div
        contenteditable="true"
        ref="content"
        :class="['expert-input', isFocus && 'is-focus']"
        @focus="isFocus = true"
        @blur="isFocus = false"
        @input="onDivInput($event)"
      >
        <p></p>
      </div>
    </div>
    {{ value }}
  </div>
</template>

<script>
export default {
  name: 'ExpertField',
  props: {
    modelValue: {type: String, default: ''},
    label: {type: String, default: ''},
    width: {type: Number, default: 320},
    hasLineNumbering: {type: Boolean, default: false},
  },
  emits: ['update:modelValue'],
  data() {
    return {
      isFocus: false,
      newValue: '',
      currentSelection: 0,
    }
  },
  computed: {
    value: {
      get() {
        return this.newValue
      },
      set(val) {
        this.newValue = val
        console.log(val)
        this.$refs.content.innerHTML = val
      },
    },
  },
  mounted() {
    console.log(this.$refs.content)
    this.value = '<p>??????</p>'
  },
  // watch: {
  //   '$refs.content'() {
  //     if (this.isClearSelectedValue) {
  //       this.value = ''
  //       this.search = ''
  //     }
  //   },
  // },
  methods: {
    onDivInput({target}) {
      console.log(target.innerHTML)
      const selection = window.getSelection().getRangeAt(0)
      // const range = document.createRange()

      console.log('on div', window.getSelection().getRangeAt(0))
      // selection.removeAllRanges()
      // range.selectNodeContents(target)
      // range.collapse(false)
      // selection.addRange(range)
      // target.focus()
      // this.value = target.innerHTML
    },

    saveSelection() {
      this.currentSelection = window.getSelection().getRangeAt(0) || 0
    },
    restoreSelection() {
      
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

  padding: 10px;
  gap: 4px;

  border-radius: var(--border-radius);
  border: 1px solid var(--input-border-color);
  background-color: #ffffff;
  outline: none;

  p {
    width: var(--expert-input-width);
    min-height: 20px;

    background-color: red;
  }
}
</style>
