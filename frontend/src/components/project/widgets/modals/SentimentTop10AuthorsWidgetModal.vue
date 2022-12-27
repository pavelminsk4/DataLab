<template>
  <BaseModal modal-frame-style="width: 50vw;">
    <div class="main-title">{{ sentimentTopAuthors.title }}</div>

    <div class="general-wrapper-settings">
      <SettingsButtons @update-setting-panel="updateSettingPanel" />

      <BasicSettingsScreen
        v-if="panelName === 'General'"
        :period="sentimentTopAuthors.aggregation_period"
        :widget-title="sentimentTopAuthors.title"
        :widget-description="sentimentTopAuthors.description"
        @save-changes="saveChanges"
      />

      <DimensionsScreen
        v-if="panelName === 'Dimensions'"
        :active-dimensions="sentimentTopAuthors"
        :project-id="projectId"
        :widget-author="sentimentTopAuthors.author_dim_pivot"
        :widget-country="sentimentTopAuthors.country_dim_pivot"
        :widget-language="sentimentTopAuthors.language_dim_pivot"
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
  name: 'SentimentTop10AuthorsWidgetModal',
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
    sentimentTopAuthors() {
      return this.widgets['sentiment_top_10_authors_widget']
    },
  },
  methods: {
    ...mapActions([
      action.UPDATE_AVAILABLE_WIDGETS,
      action.GET_AVAILABLE_WIDGETS,
      action.GET_SENTIMENT_TOP_AUTHORS,
    ]),
    async saveOptions() {
      await this[action.UPDATE_AVAILABLE_WIDGETS]({
        projectId: this.projectId,
        data: {
          sentiment_top_10_authors_widget: {
            id: this.sentimentTopAuthors.id,
            title: this.title || this.sentimentTopAuthors.title,
            description:
              this.description || this.sentimentTopAuthors.description,
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
          sentiment_top_10_authors_widget: {
            id: this.sentimentTopAuthors.id,
            title: title || this.sentimentTopAuthors.title,
            description: description || this.sentimentTopAuthors.description,
            smpl_freq:
              aggregationPeriod.toLowerCase() ||
              this.sentimentTopAuthors.smpl_freq,
          },
        },
      })
      await this[action.GET_SENTIMENT_TOP_AUTHORS](this.projectId)
      await this[action.GET_AVAILABLE_WIDGETS](this.projectId)
      this.$emit('close')
    },
    async saveDimensions(author, language, country) {
      if (author || author === '') {
        author = author || this.sentimentTopAuthors.author_dim_pivot
      }
      if (language || language === '') {
        language = language || this.sentimentTopAuthors.language_dim_pivot
      }
      if (country || country === '') {
        country = country || this.sentimentTopAuthors.country_dim_pivot
      }

      await this[action.UPDATE_AVAILABLE_WIDGETS]({
        projectId: this.projectId,
        data: {
          sentiment_top_10_authors_widget: {
            id: this.sentimentTopAuthors.id,
            smpl_freq: this.sentimentTopAuthors.aggregation_period,
            author_dim_pivot: author,
            language_dim_pivot: language,
            country_dim_pivot: country,
            sentiment_dim_pivot: this.sentimentTopAuthors.sentiment_dim_pivot,
            source_dim_pivot: this.sentimentTopAuthors.source_dim_pivot,
          },
        },
      })

      this.loading = true
      await this[action.GET_AVAILABLE_WIDGETS](this.projectId)
      await this[action.GET_SENTIMENT_TOP_AUTHORS](this.projectId)
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
