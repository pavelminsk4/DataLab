<template>
  <div class="nav-wrapper">
    <div class="title-wrapper">
      <div class="back-button" @click="backToHome">
        <ArrowLeftIcon class="arrow-back" />
        Back to Dashboard
      </div>

      <h1 class="title">{{ title }}Project name</h1>

      <div class="hint">
        Set up alerts for your project with highly customized filters
      </div>
    </div>
    <BaseButton class="button"> Save </BaseButton>
  </div>
</template>

<script>
import BaseButton from '@components/buttons/BaseButton'

import ArrowLeftIcon from '@components/icons/ArrowLeftIcon'

export default {
  name: 'ProjectNav',
  components: {BaseButton, ArrowLeftIcon},
  props: {
    title: {
      type: String,
      default: '',
    },
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
.nav-wrapper {
  display: flex;
  justify-content: space-between;

  align-items: center;
}

.title-wrapper {
  display: flex;
  flex-direction: column;
}

.back-button {
  cursor: pointer;

  margin-bottom: 10px;

  font-style: normal;
  font-weight: 400;
  font-size: 14px;
  line-height: 20px;
  color: var(--primary-button-color);
}

.arrow-back {
  color: var(--primary-button-color);
}

.title {
  margin-bottom: 6px;

  font-style: normal;
  font-weight: 600;
  font-size: 36px;
  line-height: 54px;
  color: var(--primary-text-color);
}

.hint {
  font-style: normal;
  font-weight: 400;
  font-size: 14px;
  line-height: 20px;
  color: var(--secondary-text-color);
}

.button {
  width: 117px;
}
</style>
