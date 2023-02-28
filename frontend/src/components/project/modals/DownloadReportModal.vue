<template>
  <BaseModal
    modal-frame-style="width: auto; height: auto;"
    title="Download Report"
  >
    <div class="reports-wrapper">
      <section class="form-section">
        <div class="title-section">
          <h3>Instant Report</h3>
          <div class="regular-report-link">
            Go to Regular Report <LinkArrowIcon />
          </div>
        </div>

        <div class="form">
          <DivWithError
            :hasError="!!errors.layoutElementsError"
            :errorMessage="errors.layoutElementsError"
            class="layout-elements"
          >
            <div class="settings-name">Layout Elements</div>
            <BaseCheckbox
              v-for="(item, index) in layoutElements"
              :key="'layoutEl' + index"
              v-model="layout"
              :id="item.value"
              :class="[
                'checkbox',
                isSelectedItem(item.value) && 'active-element',
              ]"
            >
              {{ item.value }}
            </BaseCheckbox>
          </DivWithError>

          <DivWithError
            :hasError="!!errors.languageError"
            :errorMessage="errors.languageError"
            class="layout-elements"
          >
            <div class="settings-name">Language</div>

            <BaseRadio
              v-for="(item, index) in language"
              :key="item + index"
              v-model="selectedLanguageProxy"
              :checked="item"
              :value="item"
              :id="item + index"
              :label="item"
              class="radio-btn"
            />
          </DivWithError>

          <DivWithError
            :hasError="!!errors.formatError"
            :errorMessage="errors.formatError"
            class="layout-elements"
          >
            <div class="settings-name">Format</div>
            <BaseRadio
              v-for="(item, index) in format"
              :key="item + index"
              v-model="selectedFormatProxy"
              :checked="item"
              :value="item"
              :id="item + index"
              :label="item"
              class="radio-btn"
            />
          </DivWithError>

          <BaseSelect
            v-model="template"
            placeholder="Select Template"
            select-title="Template"
            name="template"
            :list="titleTemplates"
            :is-reject-selection="false"
            :hasError="!!errors.templateError"
            :errorMessage="errors.templateError"
            class="select"
            @select-option="selectItem"
          />

          <BaseButton
            :buttonLoading="loading"
            class="link"
            @click="downloadReport"
          >
            <ReportsUploadIcon />
            Download Report
          </BaseButton>
        </div>
      </section>
      <section class="icon-wrapper">
        <ReportsIcon />
      </section>
    </div>
  </BaseModal>
</template>

<script>
import {mapActions, mapGetters, mapState} from 'vuex'
import {action, get} from '@store/constants'

import BaseRadio from '@/components/BaseRadio'
import BaseButton from '@/components/common/BaseButton'
import BaseSelect from '@/components/BaseSelect'
import BaseModal from '@/components/modals/BaseModal'
import DivWithError from '@/components/DivWithError'
import BaseCheckbox from '@/components/BaseCheckbox2'
import LinkArrowIcon from '@/components/icons/LinkArrowIcon'
import ReportsUploadIcon from '@/components/icons/ReportsUploadIcon'
import ReportsIcon from '@/components/icons/ReportsIcon'

export default {
  name: 'DownloadReportModal',
  components: {
    ReportsIcon,
    ReportsUploadIcon,
    BaseButton,
    BaseSelect,
    BaseRadio,
    BaseCheckbox,
    DivWithError,
    BaseModal,
    LinkArrowIcon,
  },
  props: {
    projectId: {
      type: [Number, String],
      required: true,
    },
  },
  data() {
    return {
      newTemplate: '',
      layoutElements: [
        {value: 'Table Content', key: 'report_table_content'},
        {value: 'Widgets', key: 'report_widgets'},
        {value: 'Content', key: 'report_content'},
      ],
      language: ['English', 'Arabic'],
      format: ['PDF', 'DOC'],
      layoutKeys: [],
      errors: {
        templateError: null,
        layoutElementsError: null,
        formatError: null,
        languageError: null,
      },
      selectedLayout: [],
      selectedLanguage: '',
      selectedFormat: '',
    }
  },
  computed: {
    ...mapState(['loading']),
    ...mapGetters({
      templates: get.TEMPLATES,
    }),
    titleTemplates() {
      return this.templates.map((el) => el.title)
    },
    layout: {
      get() {
        return this.selectedLayout
      },
      set(val) {
        this.selectedLayout = val
        this.errors.layoutElementsError = null
      },
    },
    template: {
      get() {
        return this.newTemplate
      },
      set(val) {
        this.newTemplate = val
        this.errors.templateError = null
      },
    },
    selectedLanguageProxy: {
      get() {
        return this.selectedLanguage
      },
      set(val) {
        this.selectedLanguage = val
        this.errors.languageError = null
      },
    },
    selectedFormatProxy: {
      get() {
        return this.selectedFormat
      },
      set(val) {
        this.selectedFormat = val
        this.errors.formatError = null
      },
    },
  },
  created() {
    this[action.GET_TEMPLATES]()
  },
  methods: {
    ...mapActions([
      action.GET_TEMPLATES,
      action.UPDATE_PROJECT,
      action.GET_INSTANTLY_REPORT,
    ]),
    isSelectedItem(item) {
      return this.layout.some((el) => item === el)
    },
    selectItem(name, val) {
      let element = this.templates.filter((el) => el.title === val)
      this.template = element[0]
    },
    saveTemplate() {
      if (!this.validationForm()) return

      try {
        this[action.UPDATE_PROJECT]({
          projectId: this.projectId,
          data: {
            report_template: this.template.id,
            report_format: this.selectedFormatProxy,
            report_language: this.selectedLanguageProxy,
            ...this.layoutKeys,
          },
        })
      } catch (e) {
        console.log(e)
      }
    },
    validationForm() {
      const defaultErrorMessage = 'required'

      this.errors.templateError = this.template ? null : defaultErrorMessage
      this.errors.layoutElementsError = this.layout.length
        ? null
        : defaultErrorMessage
      this.errors.formatError = this.selectedFormatProxy
        ? null
        : defaultErrorMessage
      this.errors.languageError = this.selectedLanguageProxy
        ? null
        : defaultErrorMessage

      return (
        !this.errors.templateError &&
        !this.errors.layoutElementsError &&
        !this.errors.formatError &&
        !this.errors.languageError
      )
    },
    async downloadReport() {
      this.saveTemplate()

      if (!this.validationForm()) return

      this.loading = true
      try {
        const res = await this[action.GET_INSTANTLY_REPORT](this.projectId)

        const anchor = document.createElement('a')
        anchor.href = res
        anchor.download = 'instant_report.pdf'

        document.body.appendChild(anchor)
        anchor.click()
        document.body.removeChild(anchor)
      } catch (error) {
        console.log(error)
      } finally {
        this.loading = false
      }
    },
  },
}
</script>

<style lang="scss" scoped>
.reports-wrapper {
  display: flex;

  margin: -24px;

  .form-section {
    display: flex;
    flex-direction: column;

    padding: 24px;

    border-right: 1px solid var(--border-color);

    .title-section {
      display: flex;
      justify-content: space-between;
      align-items: center;

      .regular-report-link {
        display: flex;
        align-items: center;
        gap: 10px;

        margin-left: 22px;

        cursor: pointer;
        color: var(--primary-color);

        &:hover {
          text-decoration: underline;
        }
      }
    }

    .form {
      display: flex;
      flex-direction: column;
      gap: 32px;

      margin-top: 28px;

      .layout-elements {
        display: flex;
        flex-direction: column;
        gap: 12px;

        .checkbox {
          gap: 10px;
          padding: 14px;

          border-radius: 10px;
          border: 1px solid var(--border-color);

          font-style: normal;
          font-weight: 400;
          font-size: 14px;
          line-height: 20px;
          color: var(--typography-title-color);
        }

        .active-element {
          border: 1px solid var(--border-active-color);
          background-color: var(--primary-active-color);
        }

        .radio-btn {
          width: 100%;
        }
      }

      .setting-name {
        font-style: normal;
        font-weight: 400;
        font-size: 14px;
        line-height: 20px;
        color: var(--typography-title-color);
      }

      .link {
        display: flex;
        align-self: flex-end;

        width: 170px;
      }
    }
  }

  .icon-wrapper {
    padding: 36px 34px 0;

    background-color: var(--background-primary-color);
  }
}
</style>
