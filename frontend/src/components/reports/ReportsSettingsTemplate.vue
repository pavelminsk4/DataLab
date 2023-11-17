<template>
  <aside class="wrapper">
    <CustomText tag="h4" text="Settings Template" class="wrapper__title" />

    <section class="setting">
      <CustomText tag="span" text="Language" class="setting__title" />
      <BaseRadio v-model="language" value="English" label="English" />
    </section>

    <section class="setting">
      <CustomText tag="span" text="Format" class="setting__title" />
      <BaseRadio v-model="format" value="PDF" label="PDF" />
      <BaseRadio v-model="format" value="DOC" label="DOC" />
    </section>

    <section class="setting">
      <CustomText tag="span" text="Template" class="setting__title" />
      <BaseSelect
        v-model="template"
        :options="templatesOptions"
        select-name="template"
      />
    </section>
  </aside>
</template>

<script>
import {action} from '@store/constants'
import {mapActions} from 'vuex'
import createReportMixin from '@/lib/mixins/create-report.js'

import CustomText from '@/components/CustomText'
import BaseRadio from '@/components/BaseRadio'
import BaseSelect from '@/components/BaseSelect2'

export default {
  name: 'ReportsSettingsTemplate',
  mixins: [createReportMixin],
  components: {BaseRadio, BaseSelect, CustomText},
  data() {
    return {
      newLanguage: '',
      newFormat: '',
      newTemplate: 'Select template',
      templates: [],
    }
  },
  computed: {
    language: {
      get() {
        return this.newLanguage || this.newReport.report_language
      },
      set(val) {
        this.newLanguage = val
        this[action.UPDATE_NEW_REPORT]({
          report_language: val,
        })
      },
    },
    format: {
      get() {
        return this.newFormat || this.newReport.report_format
      },
      set(val) {
        this.newFormat = val
        this[action.UPDATE_NEW_REPORT]({
          report_format: val,
        })
      },
    },
    templatesOptions() {
      return this.templates.map((template) => template.title)
    },
    template: {
      get() {
        const defaultTemplate = 'Select template'
        const currentTemplate = this.templates.find(
          (template) => template.id === this.newReport.report_template
        )?.title
        return currentTemplate || defaultTemplate
      },
      set(val) {
        const templateId = this.templates.find(
          (template) => template.title === val
        ).id
        this[action.UPDATE_NEW_REPORT]({
          report_template: templateId,
        })
      },
    },
  },
  async created() {
    this.templates = await this[action.GET_TEMPLATES]()
  },
  methods: {
    ...mapActions([action.GET_TEMPLATES]),
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
