<template>
  <aside class="wrapper">
    <h4 class="wrapper__title">Settings Template</h4>

    <section class="setting">
      <span class="setting__title">Language</span>
      <BaseRadio v-model="language" value="English" label="English" />
    </section>

    <section class="setting">
      <span class="setting__title">Format</span>
      <BaseRadio v-model="format" value="PDF" label="PDF" />
      <BaseRadio v-model="format" value="DOC" label="DOC" />
    </section>

    <section class="setting">
      <span class="setting__title">Template</span>
      <BaseSelect
        v-model="template"
        :options="options"
        select-name="template"
      />
    </section>
  </aside>
</template>

<script>
import {action} from '@store/constants'
import createReportMixin from '@/lib/mixins/create-report.js'

import BaseRadio from '@/components/BaseRadio'
import BaseSelect from '@/components/BaseSelect2'
export default {
  name: 'ReportsSettingsTemplate',
  mixins: [createReportMixin],
  components: {BaseRadio, BaseSelect},
  data() {
    return {
      newLanguage: '',
      newFormat: '',
      newTemplate: 'Select template',
    }
  },
  computed: {
    language: {
      get() {
        return this.newLanguage || this.newReport.language
      },
      set(val) {
        this.newLanguage = val
        this[action.UPDATE_NEW_REPORT]({
          language: val,
        })
      },
    },
    format: {
      get() {
        return this.newFormat || this.newReport.format
      },
      set(val) {
        this.newFormat = val
        this[action.UPDATE_NEW_REPORT]({
          format: val,
        })
      },
    },
    template: {
      get() {
        return this.newTemplate || this.newReport.template
      },
      set(val) {
        this.newTemplate = val
        this[action.UPDATE_NEW_REPORT]({
          template: val,
        })
      },
    },
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
