<template>
  <aside class="wrapper">
    <h4 class="wrapper__title">Settings Template</h4>

    <section class="setting">
      <span class="setting__title">Language</span>
      <BaseRadio v-model="settings.language" value="English" label="English" />
      <BaseRadio v-model="settings.language" value="Arabic" label="Arabic" />
    </section>

    <section class="setting">
      <span class="setting__title">Format</span>
      <BaseRadio v-model="settings.format" value="PDF" label="PDF" />
      <BaseRadio v-model="settings.format" value="DOC" label="DOC" />
    </section>

    <section class="setting">
      <span class="setting__title">Template</span>
    </section>
  </aside>
</template>

<script>
import BaseRadio from '@/components/BaseRadio'
export default {
  components: {BaseRadio},
  data() {
    return {
      settings: {
        language: 'English',
        format: 'PDF',
        template: 'Select template',
      },
    }
  },
}
</script>

<style lang="scss" scoped>
.wrapper {
  display: flex;
  flex-direction: column;
  gap: 20px;

  &__title {
    font-size: 16px;
    font-weight: 500 !important;
  }

  .setting {
    display: flex;
    flex-direction: column;
    gap: 10px;
    margin-bottom: 10px;

    width: 80%;

    .base-radio-container {
      width: 100%;
    }
  }
}
</style>
