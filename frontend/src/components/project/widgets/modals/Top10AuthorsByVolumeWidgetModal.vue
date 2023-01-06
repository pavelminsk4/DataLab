<template>
  <BaseModal modal-frame-style="width: 50vw;">
    <div class="main-title">{{ topAuthors.title }}</div>

    <div class="general-wrapper-settings">
      <SettingsButtons @update-setting-panel="updateSettingPanel" />

      <BasicSettingsScreen
        v-if="panelName === 'General'"
        :period="topAuthors.aggregation_period"
        :widget-title="topAuthors.title"
        :widget-description="topAuthors.description"
        @save-changes="saveChanges"
      />

      <DimensionsScreen
        v-if="panelName === 'Dimensions'"
        :active-dimensions="topAuthors"
        :project-id="projectId"
        :widget-author="topAuthors.author_dim_pivot"
        :widget-country="topAuthors.country_dim_pivot"
        :widget-language="topAuthors.language_dim_pivot"
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
  name: 'Top10AuthorsByVolumeWidgetModal',
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
    topAuthors() {
      return this.widgets['top_10_authors_by_volume_widget']
    },
  },
  methods: {
    ...mapActions([
      action.UPDATE_AVAILABLE_WIDGETS,
      action.GET_AVAILABLE_WIDGETS,
      action.GET_TOP_AUTHORS_WIDGET,
    ]),
    async saveOptions() {
      await this[action.UPDATE_AVAILABLE_WIDGETS]({
        projectId: this.projectId,
        data: {
          top_10_authors_by_volume_widget: {
            id: this.topAuthors.id,
            title: this.title || this.topAuthors.title,
            description: this.description || this.topAuthors.description,
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
          top_10_authors_by_volume_widget: {
            id: this.topAuthors.id,
            title: title || this.topAuthors.title,
            description: description || this.topAuthors.description,
            aggregation_period:
              aggregationPeriod.toLowerCase() ||
              this.topAuthors.aggregation_period,
          },
        },
      })
      await this[action.GET_TOP_AUTHORS_WIDGET](this.projectId)
      await this[action.GET_AVAILABLE_WIDGETS](this.projectId)
      this.$emit('close')
    },
    async saveDimensions(author, language, country) {
      if (author || author === '') {
        author = author || this.topAuthors.author_dim_pivot
      }
      if (language || language === '') {
        language = language || this.topAuthors.language_dim_pivot
      }
      if (country || country === '') {
        country = country || this.topAuthors.country_dim_pivot
      }

      await this[action.UPDATE_AVAILABLE_WIDGETS]({
        projectId: this.projectId,
        data: {
          top_10_authors_by_volume_widget: {
            id: this.topAuthors.id,
            aggregation_period: this.topAuthors.aggregation_period,
            author_dim_pivot: author,
            language_dim_pivot: language,
            country_dim_pivot: country,
            sentiment_dim_pivot: this.topAuthors.sentiment_dim_pivot,
            source_dim_pivot: this.topAuthors.source_dim_pivot,
          },
        },
      })

      await this[action.GET_AVAILABLE_WIDGETS](this.projectId)
      await this[action.GET_TOP_AUTHORS_WIDGET](this.projectId)
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
