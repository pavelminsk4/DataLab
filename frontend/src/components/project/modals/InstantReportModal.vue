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
        @select-option="selectItem"
        class="select"
      />

      <BaseButton
        :is-not-background="true"
        @click="saveTemplate"
        class="button"
      >
        Save Template
      </BaseButton>

      <a class="link" :href="`/projects/${projectId}/reports/instantly_report`">
        Download
      </a>
    </div>

    <div class="layout-settings-wrapper">
      <div class="layout-elements">
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
      </div>

      <div class="general-settings">
        <div class="general-item">
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
        </div>

        <div class="general-item">
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
        </div>
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

export default {
  name: 'InstantReportModal',
  components: {
    BaseRadio,
    BaseCheckbox,
    BaseSelect,
    BaseButton,
    BaseModal,
  },
  props: {
    projectId: {
      type: [Number, String],
      required: true,
    },
  },
  data() {
    return {
      template: '',
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
    selectedFormatProxy: {
      get() {
        return this.selectedFormat
      },
      set(format) {
        this.selectedFormat = format
      },
    },
    selectedLanguageProxy: {
      get() {
        return this.selectedLanguage
      },
      set(language) {
        this.selectedLanguage = language
      },
    },
  },
  methods: {
    ...mapActions([action.GET_TEMPLATES, action.UPDATE_PROJECT]),
    selectItem(name, val) {
      let element = this.templates.filter((el) => el.title === val)
      this.template = element[0]
    },
    saveTemplate() {
      this[action.UPDATE_PROJECT]({
        projectId: this.projectId,
        data: {
          report_template: this.template.id,
          report_format: this.selectedFormat,
          report_language: this.selectedLanguage,
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
    flex-shrink: 0;

    padding: 32px;

    background: #1d1e1f;
    border-radius: 15px;

    .checkbox {
      margin-top: 11px;
    }
  }

  .general-settings {
    display: flex;

    width: 100%;
    padding: 32px;

    background: #1d1e1f;
    border-radius: 15px;

    .general-item {
      margin-right: 60px;
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
