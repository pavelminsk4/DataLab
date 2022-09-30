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
          <CheckIcon v-if="item.isFinished" />
          <span v-else>{{ item.value }}</span>
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

import CheckIcon from '@components/icons/CheckIcon'
import ArrowLeftIcon from '@components/icons/ArrowLeftIcon'
import OnlineRadioIcon from '@/components/icons/OnlineRadioIcon'

export default {
  name: 'StepsNav',
  components: {OnlineRadioIcon, BaseButton, CheckIcon, ArrowLeftIcon},
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
    ...mapState(['newProject']),
    progressBarData() {
      return this.isExistingWorkspace
        ? [
            {
              name: 'ProjectStep1',
              value: 1,
              isFinished: false,
            },
            {
              name: 'ProjectStep2',
              value: 2,
              isFinished: false,
            },
          ]
        : [
            {
              name: 'Step1',
              value: 1,
              isFinished: false,
            },
            {
              name: 'Step2',
              value: 2,
              isFinished: false,
            },
            {
              name: 'Step3',
              value: 3,
              isFinished: false,
            },
          ]
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
  cursor: pointer;

  color: var(--secondary-text-color);
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
