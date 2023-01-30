<template>
  <BaseModal modal-frame-style="width: auto; height: auto;">
    <div class="title">Template settings</div>

    <div class="wrapper-buttons">
      <BaseSelect
        v-model="template"
        placeholder="Select Template"
        name="template"
        :list="titleTemplates"
        :is-reject-selection="false"
        :hasError="!!errors.templateError"
        :errorMessage="errors.templateError"
        class="select"
        @select-option="selectItem"
      />

      <BaseButton
        :is-not-background="true"
        @click="saveTemplate"
        class="button"
      >
        Save Template
      </BaseButton>

      <BaseButton :buttonLoading="loading" class="link" @click="downloadReport">
        Download
      </BaseButton>
    </div>

    <div class="layout-settings-wrapper">
      <DivWithError
        :hasError="!!errors.layoutElementsError"
        :errorMessage="errors.layoutElementsError"
        class="layout-elements"
      >
        <div class="settings-name">Layout Elements</div>
        <BaseCheckbox
          v-for="(item, index) in layoutElements"
          :key="'layoutEl' + index"
          :id="item.value"
          @change="onChange"
          class="checkbox"
        >
          <span class="name">{{ item.value }}</span>
        </BaseCheckbox>
      </DivWithError>

      <div class="general-settings">
        <DivWithError
          :hasError="!!errors.formatError"
          :errorMessage="errors.formatError"
          class="general-item"
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

        <DivWithError
          :hasError="!!errors.languageError"
          :errorMessage="errors.languageError"
          class="general-item"
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
      </div>
    </div>
  </BaseModal>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'

import BaseRadio from '@/components/BaseRadio'
import BaseSelect from '@/components/BaseSelect'
import BaseModal from '@/components/modals/BaseModal'
import BaseButton from '@/components/buttons/BaseButton'
import BaseCheckbox from '@/components/BaseCheckbox'
import DivWithError from '@/components/DivWithError'

export default {
  name: 'InstantReportModal',
  components: {
    BaseRadio,
    BaseCheckbox,
    BaseSelect,
    BaseButton,
    BaseModal,
    DivWithError,
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
      format: ['PDF', 'DOC'],
      language: ['English', 'Arabic'],
      contentProperties: [
        'Content Title',
        'Author Name',
        'Content Sentiment',
        'Clout Score',
        'Source Global Rank',
        ' Source Brand Name',
        'Content (first sentence)',
        'Content Synopsis',
        'Time Published',
        'Media Channel',
        'Content Potential Reach',
        'Source Icon',
        'Source Country',
        'Followers',
        'Source Audience',
        'Content Featured Image',
        'Content (first Paragraph)',
        'Post User Categories',
        'Author Picture',
        'Media Channel Type',
        'Content AVE',
        'Content Sentiment',
        'Source Name',
        'Source Location',
        'Source Domestik Rank',
        'Source Site Name',
        'Content (excerpt)',
        'Content Synopsis Tite',
        'Screen Capture',
        'Post Related Articles',
      ],
      selectedFormat: '',
      selectedLanguage: '',
      collectionProxy: [],
      collectionProperties: [],
      layoutKeys: [],
      errors: {
        templateError: null,
        layoutElementsError: null,
        formatError: null,
        languageError: null,
      },
      loading: false,
    }
  },
  created() {
    this[action.GET_TEMPLATES]()
  },
  computed: {
    ...mapGetters({
      templates: get.TEMPLATES,
    }),
    titleTemplates() {
      return this.templates.map((el) => el.title)
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
    selectedFormatProxy: {
      get() {
        return this.selectedFormat
      },
      set(val) {
        this.selectedFormat = val
        this.errors.formatError = null
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
  },
  methods: {
    ...mapActions([
      action.GET_TEMPLATES,
      action.UPDATE_PROJECT,
      action.GET_INSTANTLY_REPORT,
    ]),
    selectItem(name, val) {
      let element = this.templates.filter((el) => el.title === val)
      this.template = element[0]
    },
    saveTemplate() {
      if (!this.validationForm()) return

      this[action.UPDATE_PROJECT]({
        projectId: this.projectId,
        data: {
          report_template: this.template.id,
          report_format: this.selectedFormatProxy,
          report_language: this.selectedLanguageProxy,
          ...this.layoutKeys,
        },
      })
    },
    onChange(args) {
      const {id, checked} = args
      if (checked) {
        this.collectionProxy.push(args)
      } else {
        let element = this.collectionProxy.indexOf(id)
        this.removeSelectedFilter(element, id)
      }
      this.errors.layoutElementsError = null
    },
    onChangeProperties(args) {
      const {id, checked} = args
      if (checked) {
        this.collectionProperties.push(id)
      } else {
        let element = this.collectionProperties.indexOf(id)
        this.removeSelected(element, id)
      }
    },
    removeSelected(index) {
      this.collectionProperties.splice(index, 1)
    },
    removeSelectedFilter(index) {
      this.collectionProxy.splice(index, 1)
    },
    validationForm() {
      const defaultErrorMessage = 'required'

      this.errors.templateError = this.template ? null : defaultErrorMessage
      this.errors.layoutElementsError = this.collectionProxy.length
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
.title {
  margin-bottom: 40px;

  font-style: normal;
  font-weight: 600;
  font-size: 36px;
  line-height: 54px;
}

.layout-settings-wrapper {
  display: flex;
  gap: 14px;

  margin: 15px 0;

  .settings-name {
    font-style: normal;
    font-weight: 500;
    font-size: 14px;
    line-height: 20px;
  }

  .layout-elements {
    --error-top: 5px;
    flex-shrink: 0;

    padding: 32px;

    background: #1d1e1f;
    border: 1px solid #1d1e1f;
    border-radius: 15px;

    .checkbox {
      margin-top: 11px;
    }
  }

  .general-settings {
    display: flex;

    width: 100%;

    background: #1d1e1f;
    border-radius: 15px;

    .general-item {
      --error-top: 5px;
      padding: 32px;

      border: 1px solid #1d1e1f;
      border-radius: 15px;
    }
  }
}

.content-properties-wrapper {
  display: flex;
  flex-direction: column;
  flex-wrap: wrap;

  max-width: 100%;
  max-height: fit-content;
  padding: 30px;

  background: #1d1e1f;
  border-radius: 15px;

  .content-properties-title {
    min-width: 100%;
    padding-bottom: 18px;
    margin-bottom: 22px;

    border-bottom: 1px solid var(--input-border-color);

    font-style: normal;
    font-weight: 600;
    font-size: 16px;
    line-height: 22px;
    color: var(--primary-text-color);
  }

  .properties-checkboxes {
    display: flex;
    flex-direction: column;
    flex-wrap: wrap;
    gap: 15px 30px;

    max-height: 400px;
  }
}

.wrapper-buttons {
  display: flex;
  gap: 14px;

  .select {
    width: 408px;
  }

  .button {
    width: 160px;
  }

  .link {
    display: flex;

    text-decoration: none;

    width: 128px;
    padding: 10px 30px;

    background: var(--primary-button-color);
    border-radius: 8px;

    color: var(--primary-text-color);

    font-style: normal;
    font-weight: 600;
    font-size: 14px;
    line-height: 20px;

    &:hover {
      background: rgba(5, 95, 252, 0.6);
    }
  }
}

.radio-btn {
  display: flex;

  margin: 12px 0 0;

  color: var(--primary-text-color);

  cursor: pointer;
}

.name {
  margin-left: 10px;

  font-style: normal;
  font-weight: 400;
  font-size: 14px;
  line-height: 20px;
}
</style>

<style>
.additional-key > .input-tag {
  margin-bottom: 10px;
}
</style>
