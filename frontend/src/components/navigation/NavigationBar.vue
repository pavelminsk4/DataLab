<template>
  <div class="back-button" @click="backToPage">
    <ArrowLeftIcon class="arrow-back" />
    <span v-if="!!step || isBackToDashboard">Back to dashboard</span>
    <span v-else>Back to workspace</span>
  </div>

  <div class="create-project-title">
    <div class="title-wrapper">
      <h1 class="title">{{ title }}</h1>
      <div class="search-results">{{ searchResults }} results</div>
    </div>
    <div class="content-bar-wrapper">
      <Steps
        v-if="!!step"
        :step="step"
        :current-step="currStep"
        :is-existing-workspace="isExistingWorkspace"
      />
      <BaseButton
        v-if="!!step"
        :is-disabled="!isActiveButton"
        :style="`width: ${buttonWidth}`"
        :button-loading="buttonLoading"
        class="next-button"
        @click="goToNextStep"
      >
        {{ buttonName }}
      </BaseButton>

      <slot></slot>
    </div>
  </div>
  <div class="hint">{{ hint }}</div>
</template>

<script>
import {get} from '@store/constants'
import {mapGetters} from 'vuex'

import BaseButton from '@components/buttons/BaseButton'

import ArrowLeftIcon from '@components/icons/ArrowLeftIcon'
import Steps from '@/components/navigation/Steps'

export default {
  name: 'NavigationBar',
  components: {
    Steps,
    BaseButton,
    ArrowLeftIcon,
  },
  props: {
    title: {
      type: String,
      default: '',
    },
    hint: {
      type: String,
      default: '',
    },
    step: {
      type: String,
      required: false,
    },
    isActiveButton: {
      type: Boolean,
      default: false,
    },
    buttonName: {
      type: String,
      default: 'Next',
    },
    isExistingWorkspace: {
      type: Boolean,
      default: false,
    },
    isBackToDashboard: {
      type: Boolean,
      default: false,
    },
    buttonWidth: {
      type: Number,
      default: 114,
    },
    currentProject: {
      type: String,
      default: '',
    },
    buttonLoading: {
      type: Boolean,
      default: false,
    },
    searchResults: {
      type: Number,
      required: false,
    },
  },
  emits: {
    'next-step': null,
    'click-button': null,
  },
  computed: {
    ...mapGetters({
      newProject: get.NEW_PROJECT,
      currentStep: get.CURRENT_STEP,
    }),
    currStep() {
      return this.currentStep
        .split('')
        .splice(this.currentStep.length - 1, 1)
        .join()
    },
  },
  methods: {
    backToPage() {
      if (this.step || this.isBackToDashboard) {
        this.$router.push({
          name: 'Home',
        })
      } else {
        this.$router.push({
          name: 'Workspace',
        })
      }
    },

    goToNextStep() {
      this.$emit('next-step')
      this.$emit('click-button')
    },
  },
}
</script>

<style lang="scss" scoped>
.back-button {
  display: flex;
  align-items: center;

  max-width: fit-content;

  cursor: pointer;

  font-style: normal;
  font-weight: 500;
  font-size: 11px;
  line-height: 12px;
  color: var(--typography-secondary-color);

  &:hover {
    color: var(--button-primary-color);
  }
}

.arrow-back {
  margin-right: 6px;
}

.create-project-title {
  display: flex;
  flex-direction: column;
}

.title-wrapper {
  display: flex;
  align-items: center;

  .title {
    margin: 0 12px 4px 0;

    color: var(--typography-title-color);

    font-size: 36px;
  }

  .search-results {
    font-style: normal;
    font-weight: 600;
    font-size: 14px;
    line-height: 20px;
    color: var(--typography-secondary-color);
  }
}

.content-bar-wrapper {
  display: flex;
}

.active-item {
  border: 1px solid var(--button-primary-color);
  box-shadow: 0 0 3px var(--box-shadow-color);
}

.hint {
  color: var(--typography-secondary-color);

  font-size: 14px;
}
</style>
