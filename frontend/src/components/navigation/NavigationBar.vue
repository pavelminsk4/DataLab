<template>
  <div class="back-button" @click="backToPage">
    <ArrowLeftIcon class="arrow-back" />
    <span v-if="!!step">Back to dashboard</span>
    <span v-else>Back</span>
  </div>

  <div class="create-project-title">
    <div class="title-wrapper">
      <h1 class="title">{{ title }}</h1>
      <div v-if="newProject.source || currentProject" class="source-type">
        <OnlineRadioIcon class="icon" />{{ newProject.source }}
      </div>
    </div>
    <div class="progress-bar-wrapper">
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
import {mapState} from 'vuex'

import BaseButton from '@components/buttons/BaseButton'

import ArrowLeftIcon from '@components/icons/ArrowLeftIcon'
import OnlineRadioIcon from '@/components/icons/OnlineRadioIcon'
import Steps from '@/components/navigation/Steps'

export default {
  name: 'NavigationBar',
  components: {
    Steps,
    OnlineRadioIcon,
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
      default: true,
    },
    buttonName: {
      type: String,
      default: 'Next',
    },
    isExistingWorkspace: {
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
  },
  emits: {
    'next-step': null,
    'click-button': null,
  },
  computed: {
    ...mapState(['newProject', 'currentStep']),
    currStep() {
      return this.currentStep
        .split('')
        .splice(this.currentStep.length - 1, 1)
        .join()
    },
  },
  methods: {
    backToPage() {
      if (this.step) {
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
  max-width: fit-content;

  cursor: pointer;

  color: var(--secondary-text-color);

  &:hover {
    color: var(--primary-button-color);
  }
}

.arrow-back {
  margin-right: 6px;
}

.create-project-title {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.title-wrapper {
  display: flex;
  align-items: center;

  .title {
    margin: 5px 0 2px;

    color: var(--primary-text-color);

    font-size: 36px;
  }

  .source-type {
    display: flex;
    align-items: center;

    margin-left: 23px;
    padding: 4px 12px 4px 17px;

    border-radius: 9px;
    background-color: rgba(5, 95, 252, 0.1);

    font-style: normal;
    font-weight: 400;
    font-size: 14px;
    line-height: 22px;
    color: var(--primary-text-color);

    .icon {
      width: 15px;
      height: 15px;
      margin-right: 7px;
    }
  }
}

.progress-bar-wrapper {
  display: flex;
  align-items: center;
  justify-content: center;
}

.active-item {
  border: 1px solid var(--primary-button-color);
  box-shadow: 0 0 3px var(--box-shadow-color);
}

.hint {
  color: var(--secondary-text-color);

  font-size: 14px;
}
</style>
