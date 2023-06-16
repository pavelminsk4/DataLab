<template>
  <div class="container">
    <div class="calendar">
      <CommonCalendar width="100%" position="bottom" />
    </div>
    <div>
      <span>Topic query</span>
      <div class="expert-area">
        <div class="line-numbers" id="line-numbers" />
        <div class="custom-textarea">
          <div
            v-html="highlightedSyntax"
            ref="highlighted"
            :class="['highlighted', bracketsError.isError && 'textarea-error']"
          />
          <textarea
            v-model="textAreaValue"
            ref="textarea"
            id="textarea"
            class="textarea"
            @input="handleInput"
          />
        </div>
        <div class="hints">
          <h4>Syntax</h4>
          <div class="hints__section">
            <span
              v-for="item in hints.syntax"
              class="hint"
              :style="{color: item.color}"
              :key="item.value"
              >{{ item.value }}</span
            >
          </div>
          <h4>Filters</h4>
          <div class="hints__section">
            <span
              v-for="item in hints.filters"
              class="hint defaultColor"
              :key="item"
              >{{ item }}</span
            >
          </div>
        </div>
      </div>
      <div :class="['no-error', bracketsError.isError && 'error']">
        <ErrorIcon />
        <span>{{ bracketsError.message }}</span>
      </div>
    </div>

    <div class="buttons">
      <BaseButton
        :is-disabled="bracketsError.isError || !textAreaValue"
        :is-not-background="true"
        class="apply-settings"
        @click="showResults"
      >
        Preview
      </BaseButton>

      <BaseButton
        :is-disabled="bracketsError.isError || !textAreaValue"
        @click="saveProject"
      >
        <SaveIcon class="save-icon" /> Save Project
      </BaseButton>
    </div>
  </div>
</template>

<script>
import BaseButton from '@/components/common/BaseButton'
import CommonCalendar from '@/components/datepicker/CommonCalendar'
import ErrorIcon from '@/components/icons/ErrorIcon'
import SaveIcon from '@/components/icons/SaveIcon'
export default {
  name: 'ExpertModeTab',
  components: {BaseButton, CommonCalendar, ErrorIcon, SaveIcon},
  props: {
    defaultQuery: {type: String, default: ''},
  },
  data() {
    return {
      bracketsError: {
        isError: false,
        message: '',
      },
      textAreaValue: '',
      highlightedSyntax: '',
    }
  },
  created() {
    this.hints = {
      syntax: [
        {value: '( )', color: '#8e00d1'},
        {value: 'OR', color: 'var(--neutral-primary-color)'},
        {value: 'AND', color: 'var(--positive-primary-color)'},
        {value: 'NOT', color: 'var(--negative-primary-color)'},
      ],
      filters: ['author', 'country', 'language', 'source', 'sentiment'],
    }
  },
  mounted() {
    if (this.defaultQuery) {
      this.validateBrackets(this.defaultQuery)
      this.textAreaValue = this.defaultQuery
      this.highlightedSyntax = this.replaceLogicalOperators(this.defaultQuery)
    }

    const lineNumbers = document.getElementById('line-numbers')
    const {textarea} = this.$refs

    const lines = []
    for (let i = 1; i < textarea.offsetHeight / 20 - 1; i++) {
      lines.push(`<span id=line-${i}>${i}</span>`)
    }
    lineNumbers.innerHTML = lines.join('')
  },

  methods: {
    validateBrackets(value) {
      const currBrackets = value
        .split('')
        .filter((el) => el === '(' || el === ')')

      let counter = 0
      currBrackets.forEach((bracket) => {
        if (bracket === '(' && counter >= 0) {
          counter++
        } else {
          counter--
        }
      })

      if (counter === 0) {
        this.bracketsError.isError = false
      } else {
        this.bracketsError.isError = true
        this.bracketsError.message =
          'Missing an ' + (counter > 0 ? 'closing' : 'opening') + ' bracket'
      }
    },

    replaceLogicalOperators(value) {
      let highlightedStr = value
      this.hints.filters.map((filter) => {
        const regex = new RegExp('\\b' + filter + '[:]', 'g')
        highlightedStr = highlightedStr.replace(
          regex,
          `<span class="defaultColor">${filter}:</span>`
        )
      })
      return highlightedStr
        .replace(/\n/g, '<br>')
        .replace(/\(/g, '<span class="expert_mode_defaultColor">(</span>')
        .replace(/\)/g, '<span class="expert_mode_defaultColor">)</span>')
        .replace(
          /\bOR\b/g,
          '<span class="defaultColor expert_mode_or">OR</span>'
        )
        .replace(
          /\bAND\b/g,
          '<span class="defaultColor expert_mode_and">AND</span>'
        )
        .replace(
          /\bNOT\b/g,
          '<span class="defaultColor expert_mode_not">NOT</span>'
        )
    },

    handleInput({target: {value}}) {
      this.validateBrackets(this.textAreaValue)
      this.highlightedSyntax = this.replaceLogicalOperators(value)
    },

    showResults() {
      if (this.bracketsError.isError) return
      this.$emit('update-query-filter', this.textAreaValue)
      this.$emit('show-result')
    },

    saveProject() {
      if (this.bracketsError.isError) return
      this.$emit('update-query-filter', this.textAreaValue)
      this.$emit('save-project')
    },
  },
}
</script>

<style lang="scss" scoped>
.container {
  display: flex;
  flex-direction: column;

  width: 95%;
  gap: 30px;
  margin: 20px 0 0 -24px;
  padding: 0 40px 0 24px;

  cursor: default;

  .calendar {
    width: 65%;
  }
  .expert-area {
    display: flex;
    gap: 5px;

    .line-numbers {
      display: flex;
      flex-direction: column;
      align-items: flex-end;

      padding: 10px 0px;
      width: 20px;

      color: var(--typography-secondary-color);
    }

    .custom-textarea {
      position: relative;

      width: 60%;
      max-height: 400px;

      .highlighted {
        position: absolute;
        overflow: hidden;

        width: 100%;
        height: 400px;
        padding: 10px;

        background: transparent;
        border: var(--border-primary);
        border-radius: var(--border-radius);
        pointer-events: none;

        word-break: break-word;
      }
      .textarea {
        overflow-y: hidden;

        width: 100%;
        height: 400px;
        padding: 10px;

        background-color: var(--background-secondary-color);
        border-radius: var(--border-radius);
        border: var(--border-primary);

        caret-color: black;
        color: transparent;
        font-size: 14px;

        resize: none;

        &:focus {
          outline: 0;
        }
      }

      .textarea-error {
        border-color: var(--primary-color);
        box-shadow: -3px -3px 0px #fcedf3, 3px -3px 0px #fcedf3,
          -3px 3px 0px #fcedf3, 3px 3px 0px #fcedf3;
      }
    }
  }

  .no-error {
    display: flex;
    align-items: center;

    margin-top: 5px;
    padding-left: 25px;
    gap: 5px;

    visibility: hidden;
    color: var(--negative-primary-color);

    svg {
      color: var(--negative-primary-color);
    }
  }

  .error {
    visibility: visible;
  }

  .hints {
    display: flex;
    flex-direction: column;

    margin-left: 20px;
    gap: 10px;

    width: 30%;

    h4 {
      font-weight: 600;
    }

    .hints__section {
      display: flex;
      flex-wrap: wrap;

      gap: 10px;

      .hint {
        padding: 4px;

        background-color: var(--background-additional-color);
        cursor: pointer;
      }
    }
  }

  .buttons {
    position: -webkit-sticky;
    position: sticky;
    bottom: -24px;

    display: flex;
    justify-content: flex-end;
    gap: 16px;

    width: 100%;
    padding: 16px;

    border-top: var(--border-primary);
    background-color: var(--background-primary-color);

    .apply-settings {
      width: 80px;
    }

    .save-icon {
      margin-right: 5px;
    }
  }
}
</style>

<style lang="scss">
.expert_mode_defaultColor {
  color: #8e00d1;
}

.expert_mode_or {
  color: var(--neutral-primary-color);
}

.expert_mode_and {
  color: var(--positive-primary-color);
}

.expert_mode_not {
  color: var(--negative-primary-color);
}
</style>
