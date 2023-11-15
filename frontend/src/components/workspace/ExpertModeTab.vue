<template>
  <div class="container">
    <div class="calendar">
      <ProjectCalendar
        :is-range="isCurrentProjectCreated"
        :start-date="startDate"
      />
    </div>
    <div :class="[isKeywordsFieldsDisable && 'disable']">
      <CustomText tag="span" text="Topic query" />
      <div class="expert-area">
        <div class="custom-textarea">
          <!-- <div
            v-html="highlightedSyntax"
            ref="highlighted"
            :class="['highlighted', bracketsError.isError && 'textarea-error']"
          /> -->
          <textarea
            v-model="textAreaValue"
            ref="textarea"
            id="textarea"
            class="textarea scroll"
            @input="handleInput"
          />
        </div>
        <div class="hints">
          <CustomText tag="h4" text="Syntax" />
          <div class="hints__section">
            <span
              v-for="item in hints.syntax"
              :key="item.value"
              :style="{color: item.color}"
              tag="span"
              class="hint"
            >
              {{ item.value }}
            </span>
          </div>
          <CustomText tag="h4" text="Filters" />
          <div class="hints__section">
            <span
              v-for="item in filters"
              :key="item"
              tag="span"
              class="hint expert-mode_defaultColor"
            >
              {{ item }}
            </span>
          </div>
        </div>
      </div>
      <div :class="['no-error', bracketsError.isError && 'error']">
        <ErrorIcon />
        <CustomText tag="span" :text="bracketsError.message" />
      </div>
    </div>

    <div class="buttons">
      <BaseButton
        v-if="moduleName === 'Social'"
        :is-disabled="bracketsError.isError || !textAreaValue"
        :is-not-background="true"
        class="apply-settings"
        @click="showResults"
      >
        <CustomText text="Preview" />
      </BaseButton>

      <BaseButton
        :is-disabled="bracketsError.isError || !textAreaValue"
        @click="saveProject"
      >
        <SaveIcon color="#ffffff" class="save-icon" />
        <CustomText text="Save Project" />
      </BaseButton>
    </div>
  </div>
</template>

<script>
import CustomText from '@components/CustomText'
import BaseButton from '@components/common/BaseButton'
import ErrorIcon from '@components/icons/ErrorIcon'
import SaveIcon from '@components/icons/SaveIcon'
import ProjectCalendar from '@components/datepicker/ProjectCalendar'

export default {
  name: 'ExpertModeTab',
  components: {
    BaseButton,
    ErrorIcon,
    SaveIcon,
    CustomText,
    ProjectCalendar,
  },
  props: {
    startDate: {type: String, required: false},
    moduleName: {type: String, required: true},
    defaultQuery: {type: String, default: ''},
    filters: {type: Array, required: true},
    isKeywordsFieldsDisable: {type: Boolean, default: false},
    isCurrentProjectCreated: {type: Boolean, default: false},
  },
  data() {
    return {
      bracketsError: {
        isError: false,
        message: '',
      },
      textAreaValue: '',
      // highlightedSyntax: '',
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
    }
  },
  mounted() {
    if (this.defaultQuery) {
      this.validateBrackets(this.defaultQuery)
      this.textAreaValue = this.defaultQuery
      // this.highlightedSyntax = this.replaceLogicalOperators(this.defaultQuery)
    }
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

    // replaceLogicalOperators(value) {
    //   let highlightedStr = value
    //   this.filters.map((filter) => {
    //     const regex = new RegExp('\\b' + filter + '[:]', 'g')
    //     highlightedStr = highlightedStr.replace(
    //       regex,
    //       `<span class="expert-mode_defaultColor">${filter}:</span>`
    //     )
    //   })
    //   return highlightedStr
    //     .replace(/\n/g, '<br>')
    //     .replace(/\(/g, '<span class="expert-mode_defaultColor">(</span>')
    //     .replace(/\)/g, '<span class="expert-mode_defaultColor">)</span>')
    //     .replace(
    //       /\bOR\b/g,
    //       '<span class="defaultColor expert-mode_or">OR</span>'
    //     )
    //     .replace(
    //       /\bAND\b/g,
    //       '<span class="defaultColor expert-mode_and">AND</span>'
    //     )
    //     .replace(
    //       /\bNOT\b/g,
    //       '<span class="defaultColor expert-mode_not">NOT</span>'
    //     )
    // },

    handleInput() {
      this.validateBrackets(this.textAreaValue)
      // this.highlightedSyntax = this.replaceLogicalOperators(value)
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
  margin: 20px 0 0 -32px;
  padding: 0 40px 0 34px;

  cursor: default;

  .calendar {
    width: 408px;
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
      height: 430px;

      overflow-y: hidden;

      .textarea {
        overflow-y: auto;

        width: 100%;
        height: 100%;
        padding: 10px;

        background-color: var(--background-secondary-color);
        border-radius: var(--border-radius);
        border: var(--border-primary);
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

<!-- .highlighted {
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
} -->
