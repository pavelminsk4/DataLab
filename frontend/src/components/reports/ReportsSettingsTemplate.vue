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
      <BaseSelect
        v-model="settings.template"
        :options="options"
        select-name="template"
      />
    </section>
  </aside>
</template>

<script>
import BaseRadio from '@/components/BaseRadio'
import BaseSelect from '@/components/BaseSelect2'
export default {
  name: 'ReportsSettingsTemplate',
  components: {BaseRadio, BaseSelect},
  data() {
    return {
      settings: {
        language: 'English',
        format: 'PDF',
        template: 'Select template',
      },
    }
  },
  created() {
    this.options = ['template_1', 'template_2', 'template_3']
  },
}
</script>

<style lang="scss" scoped>
.wrapper {
  display: flex;
  flex-direction: column;
  gap: 20px;

  width: 38vw;

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
