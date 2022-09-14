<template>
  <div class="back-button" @click="backToHome">
    <ArrowLeftIcon class="arrow-back" />
    Back
  </div>

  <div class="create-project-title">
    <H1 class="title">{{ title }}</H1>
    <div class="progress-bar-wrapper">
      <div class="progress-bar">
        <div
          v-for="(item, index) in progressBarData"
          :key="index"
          :class="['progress-item', step === item.name && 'active-item']"
        >
          <CheckIcon v-if="item.isFinished" />
          <span v-else>{{ item.value }}</span>
        </div>
      </div>
      <BaseButton
        :is-disabled="isNotActiveButton"
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
import ArrowLeftIcon from '@/components/icons/ArrowLeftIcon'
import BaseButton from '@/components/buttons/BaseButton'
import CheckIcon from '@/components/icons/CheckIcon'

export default {
  name: 'StepsNav',
  components: {CheckIcon, BaseButton, ArrowLeftIcon},
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
      default: '',
    },
    isNotActiveButton: {
      type: Boolean,
      default: false,
    },
    buttonName: {
      type: String,
      default: 'Next',
    },
  },
  data() {
    return {
      progressBarData: [
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
      ],
    }
  },
  methods: {
    backToHome() {
      this.$router.push({
        name: 'Home',
      })
    },

    goToNextStep() {
      if (this.step === 'Step1') {
        this.$emit('next-step')
      }
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

.title {
  margin: 5px 0 2px;

  color: var(--primary-text-color);

  font-size: 36px;
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
  background-color: #3e4047;

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

.next-button {
  width: 114px;
}

.hint {
  color: var(--secondary-text-color);

  font-size: 14px;
}
</style>
