<template>
  <BaseModal modal-frame-style="width: 50vw;">
    <div class="main-title">{{ sentimentTopLanguages.title }}</div>

    <div class="general-wrapper-settings">
      <SettingsButtons @update-setting-panel="updateSettingPanel" />

      <BasicSettingsScreen
        v-if="panelName === 'General'"
        :period="sentimentTopLanguages.aggregation_period"
        :widget-title="sentimentTopLanguages.title"
        :widget-description="sentimentTopLanguages.description"
        @save-changes="saveChanges"
      />

      <DimensionsScreen
        v-if="panelName === 'Dimensions'"
        :active-dimensions="sentimentTopLanguages"
        :project-id="projectId"
        :widget-author="sentimentTopLanguages.author_dim_pivot"
        :widget-country="sentimentTopLanguages.country_dim_pivot"
        :widget-language="sentimentTopLanguages.language_dim_pivot"
        @save-dimensions-settings="saveDimensions"
      />
    </div>
  </BaseModal>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'

import BaseModal from '@/components/modals/BaseModal'
import SettingsButtons from '@/components/project/widgets/modals/SettingsButtons'
import DimensionsScreen from '@/components/project/widgets/modals/screens/DimensionsScreen'
import BasicSettingsScreen from '@/components/project/widgets/modals/screens/BasicSettingsScreen'

export default {
  name: 'SentimentTop10LanguagesWidgetModal',
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
    sentimentTopLanguages() {
      return this.widgets['sentiment_top_10_languages_widget']
    },
  },
  methods: {
    ...mapActions([
      action.UPDATE_AVAILABLE_WIDGETS,
      action.GET_AVAILABLE_WIDGETS,
      action.GET_SENTIMENT_TOP_LANGUAGES,
    ]),
    async saveOptions() {
      await this[action.UPDATE_AVAILABLE_WIDGETS]({
        projectId: this.projectId,
        data: {
          sentiment_top_10_languages_widget: {
            id: this.sentimentTopLanguages.id,
            title: this.title || this.sentimentTopLanguages.title,
            description:
              this.description || this.sentimentTopLanguages.description,
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
          sentiment_top_10_languages_widget: {
            id: this.sentimentTopLanguages.id,
            title: title || this.sentimentTopLanguages.title,
            description: description || this.sentimentTopLanguages.description,
            smpl_freq:
              aggregationPeriod.toLowerCase() ||
              this.sentimentTopLanguages.smpl_freq,
          },
        },
      })
      await this[action.GET_SENTIMENT_TOP_LANGUAGES](this.projectId)
      await this[action.GET_AVAILABLE_WIDGETS](this.projectId)
      this.$emit('close')
    },
    async saveDimensions(author, language, country) {
      if (author || author === '') {
        author = author || this.sentimentTopLanguages.author_dim_pivot
      }
      if (language || language === '') {
        language = language || this.sentimentTopLanguages.language_dim_pivot
      }
      if (country || country === '') {
        country = country || this.sentimentTopLanguages.country_dim_pivot
      }

      await this[action.UPDATE_AVAILABLE_WIDGETS]({
        projectId: this.projectId,
        data: {
          sentiment_top_10_languages_widget: {
            id: this.sentimentTopLanguages.id,
            smpl_freq: this.sentimentTopLanguages.aggregation_period,
            author_dim_pivot: author,
            language_dim_pivot: language,
            country_dim_pivot: country,
            sentiment_dim_pivot: this.sentimentTopLanguages.sentiment_dim_pivot,
            source_dim_pivot: this.sentimentTopLanguages.source_dim_pivot,
          },
        },
      })

      this.loading = true
      await this[action.GET_AVAILABLE_WIDGETS](this.projectId)
      await this[action.GET_SENTIMENT_TOP_LANGUAGES](this.projectId)
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
</style>
