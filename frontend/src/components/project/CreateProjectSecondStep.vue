<template>
  <div class="back-button" @click="backToHome">
    <ArrowLeftIcon class="arrow-back" />
    Back
  </div>

  <div class="create-project-title">
    <H1 class="title">Define the search</H1>
    <div class="progress-bar-wrapper">
      <div class="progress-bar">
        <div class="progress-item">1</div>
        <div class="progress-line"></div>
        <div class="progress-item">2</div>
      </div>
      <BaseButton class="next-button" @click="$emit('next-step')">
        Save Project
      </BaseButton>
    </div>
  </div>
  <div class="hint">Search by keywords and phrases</div>

  <section class="key-word-section">
    <div class="mode-wrapper">
      <div class="mode-title mode-active">Simple mode</div>
      <div class="mode-title">Expert mode</div>
    </div>

    <div class="second-title">Define the main keywords (OR)</div>

    <BaseTag />
  </section>
</template>

<script>
import BaseButton from '@components/buttons/BaseButton'

import ArrowLeftIcon from '@components/icons/ArrowLeftIcon'
import BaseTag from '@/components/BaseTag'

export default {
  name: 'CreateProjectSecondStep',
  components: {
    BaseTag,
    BaseButton,
    ArrowLeftIcon,
  },
  methods: {
    backToHome() {
      this.$router.push({
        name: 'Home',
      })
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

.title {
  margin: 5px 0 2px;

  color: var(--primary-text-color);

  font-size: 36px;
}

.create-project-title {
  display: flex;
  justify-content: space-between;
  align-items: center;
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
  display: flex;
  align-items: center;
  justify-content: center;

  width: 24px;
  height: 24px;

  border-radius: 100%;
  border: 1px solid var(--primary-button-color);
  box-shadow: 0 0 3px var(--box-shadow-color);

  color: var(--primary-text-color);
  background-color: var(--primary-bg-color);
}

.progress-line {
  width: 34px;
  height: 2px;

  background-color: var(--progress-line);
}

.next-button {
  width: 114px;
}

.hint {
  color: var(--secondary-text-color);

  font-size: 14px;
}

.key-word-section {
  width: 515px;
  margin-top: 30px;
}

.mode-wrapper {
  display: flex;

  margin-bottom: 20px;

  border-bottom: 1px solid var(--input-border-color);
}

.mode-title {
  padding-bottom: 10px;

  font-size: 14px;
  color: rgba(255, 255, 255, 0.8);

  &:first-child {
    margin-right: 55px;
  }
}

.mode-active {
  border-bottom: 2px solid var(--primary-button-color);

  font-weight: 500;
  color: var(--primary-text-color);
}

.second-title {
  margin-bottom: 12px;

  font-size: 14px;
  color: var(--primary-text-color);
}
</style>
