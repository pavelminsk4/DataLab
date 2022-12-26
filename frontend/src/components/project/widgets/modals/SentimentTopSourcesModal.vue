<template>
  <BaseModal modal-frame-style="width: 50vw;">
    <div class="main-title">{{ sentimentTopSources.title }}</div>

    <div class="general-wrapper-settings">
      <SettingsButtons @update-setting-panel="updateSettingPanel" />

      <BasicSettingsScreen
        v-if="panelName === 'General'"
        :period="sentimentTopSources.aggregation_period"
        :widget-title="sentimentTopSources.title"
        :widget-description="sentimentTopSources.description"
        @save-changes="saveChanges"
      />

      <DimensionsScreen
        v-if="panelName === 'Dimensions'"
        :active-dimensions="sentimentTopSources"
        :project-id="projectId"
        :widget-author="sentimentTopSources.author_dim_pivot"
        :widget-country="sentimentTopSources.country_dim_pivot"
        :widget-language="sentimentTopSources.language_dim_pivot"
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
import BasicSettingsScreen from '@/components/project/widgets/modals/screens/BasicSettingsScreen'
import DimensionsScreen from '@/components/project/widgets/modals/screens/DimensionsScreen'

export default {
  name: 'SentimentTopSourcesModal',
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
    sentimentTopSources() {
      return this.widgets['sentiment_top_10_sources_widget']
    },
  },
  methods: {
    ...mapActions([
      action.UPDATE_AVAILABLE_WIDGETS,
      action.GET_AVAILABLE_WIDGETS,
      action.GET_SENTIMENT_TOP_SOURCES,
    ]),
    async saveOptions() {
      await this[action.UPDATE_AVAILABLE_WIDGETS]({
        projectId: this.projectId,
        data: {
          sentiment_top_10_sources_widget: {
            id: this.sentimentTopSources.id,
            title: this.title || this.sentimentTopSources.title,
            description:
              this.description || this.sentimentTopSources.description,
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
          sentiment_top_10_sources_widget: {
            id: this.sentimentTopSources.id,
            title: title || this.sentimentTopSources.title,
            description: description || this.sentimentTopSources.description,
            smpl_freq:
              aggregationPeriod.toLowerCase() ||
              this.sentimentTopSources.smpl_freq,
          },
        },
      })
      await this[action.GET_SENTIMENT_TOP_SOURCES](this.projectId)
      await this[action.GET_AVAILABLE_WIDGETS](this.projectId)
      this.$emit('close')
    },
    async saveDimensions(author, language, country) {
      if (author || author === '') {
        author = author || this.sentimentTopSources.author_dim_pivot
      }
      if (language || language === '') {
        language = language || this.sentimentTopSources.language_dim_pivot
      }
      if (country || country === '') {
        country = country || this.sentimentTopSources.country_dim_pivot
      }

      await this[action.UPDATE_AVAILABLE_WIDGETS]({
        projectId: this.projectId,
        data: {
          sentiment_top_10_sources_widget: {
            id: this.sentimentTopSources.id,
            smpl_freq: this.sentimentTopSources.aggregation_period,
            author_dim_pivot: author,
            language_dim_pivot: language,
            country_dim_pivot: country,
            sentiment_dim_pivot: this.sentimentTopSources.sentiment_dim_pivot,
            source_dim_pivot: this.sentimentTopSources.source_dim_pivot,
          },
        },
      })

      this.loading = true
      await this[action.GET_AVAILABLE_WIDGETS](this.projectId)
      await this[action.GET_SENTIMENT_TOP_SOURCES](this.projectId)
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
