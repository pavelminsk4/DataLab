<template>
  <div class="back-button" @click="backToHome">
    <ArrowLeftIcon class="arrow-back" />
    Back
  </div>

  <div class="create-project-title">
    <div class="title-wrapper">
      <h1 class="title">{{ title }}</h1>
      <div v-if="newProject.source" class="source-type">
        <OnlineRadioIcon class="icon" />{{ newProject.source }}
      </div>
    </div>
    <div class="progress-bar-wrapper">
      <div class="progress-bar">
        <div
          v-for="(item, index) in progressBarData"
          :key="'step' + index"
          :class="['progress-item', step === item.name && 'active-item']"
        >
          <Steps
            :hint="item.hint"
            :current-step="currStep"
            :value="item.value"
          />
        </div>
      </div>
      <BaseButton
        :is-disabled="!isActiveButton"
        :style="`width: ${buttonWidth}`"
        class="next-button"
        @click="goToNextStep"
      >
        {{ buttonName }}
      </BaseButton>
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
  name: 'StepsNav',
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
      required: true,
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
  },
  emits: {
    'next-step': null,
  },
  computed: {
    ...mapState(['newProject', 'currentStep']),
    progressBarData() {
      return this.isExistingWorkspace
        ? [
            {
              name: 'ProjectStep1',
              hint: 'Source Type',
              value: 1,
            },
            {
              name: 'ProjectStep2',
              hint: 'Keywords',
              value: 2,
            },
          ]
        : [
            {
              name: 'Step1',
              hint: 'Create Workspace',
              value: 1,
            },
            {
              name: 'Step2',
              hint: 'Source Type',
              value: 2,
            },
            {
              name: 'Step3',
              hint: 'Keywords',
              value: 3,
            },
          ]
    },
    currStep() {
      return this.currentStep
        .split('')
        .splice(this.currentStep.length - 1, 1)
        .join()
    },
  },
  methods: {
    backToHome() {
      this.$router.push({
        name: 'Home',
      })
    },

    goToNextStep() {
      this.$emit('next-step')
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

.progress-bar {
  display: flex;
  align-items: center;

  margin-right: 40px;
}

.progress-item {
  position: relative;

  display: flex;
  align-items: center;
  justify-content: center;

  width: 24px;
  height: 24px;

  border-radius: 100%;
  background-color: var(--disabled-color);

  cursor: pointer;

  color: var(--primary-text-color);

  &:not(:last-child) {
    margin-right: 38px;

    &::before {
      position: absolute;
      left: 24px;

      content: '';

      width: 38px;
      height: 2px;

      background-color: var(--progress-line);
    }
  }
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
