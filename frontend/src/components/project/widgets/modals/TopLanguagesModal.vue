<template>
  <BaseModal modal-frame-style="width: 50vw;">
    <div class="main-title">{{ topLanguages.title }}</div>

    <div class="general-wrapper-settings">
      <SettingsButtons @update-setting-panel="updateSettingPanel" />

      <BasicSettingsScreen
        v-if="panelName === 'General'"
        :period="topLanguages.aggregation_period"
        :widget-title="topLanguages.title"
        :widget-description="topLanguages.description"
        @save-changes="saveChanges"
      />

      <DimensionsScreen
        v-if="panelName === 'Dimensions'"
        :active-dimensions="topLanguages"
        :project-id="projectId"
        :widget-author="topLanguages.author_dim_pivot"
        :widget-country="topLanguages.country_dim_pivot"
        :widget-language="topLanguages.language_dim_pivot"
        @save-dimensions-settings="saveDimensions"
      />
    </div>
  </BaseModal>
</template>

<script>
import DimensionsScreen from '@/components/project/widgets/modals/screens/DimensionsScreen'
import BasicSettingsScreen from '@/components/project/widgets/modals/screens/BasicSettingsScreen'
import SettingsButtons from '@/components/project/widgets/modals/SettingsButtons'
import BaseModal from '@/components/modals/BaseModal'
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'

export default {
  name: 'TopLanguagesModal',
  components: {
    DimensionsScreen,
    BasicSettingsScreen,
    SettingsButtons,
    BaseModal,
  },
  props: {
    projectId: {
      type: Number,
      required: true,
    },
  },
  data() {
    return {
      title: '',
      description: '',
      panelName: 'General',
    }
  },
  computed: {
    ...mapGetters({widgets: get.AVAILABLE_WIDGETS, loading: get.LOADING}),
    topLanguages() {
      return this.widgets['top_10_languages_widget']
    },
  },
  methods: {
    ...mapActions([
      action.UPDATE_AVAILABLE_WIDGETS,
      action.GET_AVAILABLE_WIDGETS,
      action.GET_TOP_LANGUAGES_WIDGET,
    ]),
    async saveOptions() {
      await this[action.UPDATE_AVAILABLE_WIDGETS]({
        projectId: this.projectId,
        data: {
          top_10_languages_widget: {
            id: this.topLanguages.id,
            title: this.title || this.topLanguages.title,
            description: this.description || this.topLanguages.description,
          },
        },
      })
      await this[action.GET_AVAILABLE_WIDGETS](this.projectId)
      await this.$emit('close')
    },
    async saveChanges(title, description, aggregationPeriod) {
      this[action.UPDATE_AVAILABLE_WIDGETS]({
        projectId: this.projectId,
        data: {
          top_10_languages_widget: {
            id: this.topLanguages.id,
            title: title || this.topLanguages.title,
            description: description || this.topLanguages.description,
            smpl_freq:
              aggregationPeriod.toLowerCase() || this.topLanguages.smpl_freq,
          },
        },
      })
      await this[action.GET_TOP_LANGUAGES_WIDGET](this.projectId)
      await this[action.GET_AVAILABLE_WIDGETS](this.projectId)
      this.$emit('close')
    },
    async saveDimensions(author, language, country) {
      if (author || author === '') {
        author = author || this.topLanguages.author_dim_pivot
      }
      if (language || language === '') {
        language = language || this.topLanguages.language_dim_pivot
      }
      if (country || country === '') {
        country = country || this.topLanguages.country_dim_pivot
      }

      await this[action.UPDATE_AVAILABLE_WIDGETS]({
        projectId: this.projectId,
        data: {
          top_10_languages_widget: {
            id: this.topLanguages.id,
            smpl_freq: this.topLanguages.aggregation_period,
            author_dim_pivot: author,
            language_dim_pivot: language,
            country_dim_pivot: country,
            sentiment_dim_pivot: this.topLanguages.sentiment_dim_pivot,
            source_dim_pivot: this.topLanguages.source_dim_pivot,
          },
        },
      })

      this.loading = true
      await this[action.GET_AVAILABLE_WIDGETS](this.projectId)
      await this[action.GET_TOP_LANGUAGES_WIDGET](this.projectId)
      this.$emit('close')
    },
    updateSettingPanel(val) {
      this.panelName = val
    },
  },
}
</script>

<style lang="scss" scoped>
.main-title {
  margin-bottom: 25px;

  font-style: normal;
  font-weight: 600;
  font-size: 36px;
  line-height: 54px;
}

.input-title {
  width: 100%;
}

.description-field {
  width: 100%;
  height: 132px;
  padding: 12px 16px;
  margin-bottom: 25px;

  border: 1px solid var(--input-border-color);
  box-shadow: 0 4px 10px rgba(16, 16, 16, 0.25);
  border-radius: 10px;
  background: var(--secondary-bg-color);

  color: var(--primary-text-color);

  resize: none;
}

.description-field::placeholder {
  color: var(--secondary-text-color);
}

.description-field::-webkit-scrollbar {
  width: 10px;
}

.description-field::-webkit-scrollbar-track {
  border-radius: 10px;

  -webkit-box-shadow: inset 0 0 6px rgba(0, 0, 0, 0.3);
}

.description-field::-webkit-scrollbar-thumb {
  width: 8px;

  border-radius: 10px;

  background-color: var(--box-shadow-color);
  outline: none;
}

.settings-wrapper {
  display: flex;

  min-width: 100%;
  .options-wrapper {
    display: flex;
    flex-direction: column;

    width: 100%;

    .title-general {
      padding-bottom: 10px;
      margin-bottom: 15px;

      border-bottom: 1px solid var(--primary-button-color);

      font-weight: 400;
      font-size: 14px;
      line-height: 22px;
    }

    .title {
      margin: 25px 0 12px;

      font-style: normal;
      font-weight: 500;
      font-size: 14px;
      line-height: 110%;
    }

    .option {
      margin-bottom: 25px;
    }
  }
}
</style>
