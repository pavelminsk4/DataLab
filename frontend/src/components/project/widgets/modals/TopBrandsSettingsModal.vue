<template>
  <BaseModal modal-frame-style="width: 50vw;">
    <div class="main-title">{{ topBrands.title }}</div>

    <div class="general-wrapper-settings">
      <SettingsButtons @update-setting-panel="updateSettingPanel" />

      <BasicSettingsScreen
        v-if="panelName === 'General'"
        :period="topBrands.aggregation_period"
        :widget-title="topBrands.title"
        :widget-description="topBrands.description"
        @save-changes="saveChanges"
      />

      <DimensionsScreen
        v-if="panelName === 'Dimensions'"
        :active-dimensions="topBrands"
        :project-id="projectId"
        :widget-author="topBrands.author_dim_pivot"
        :widget-country="topBrands.country_dim_pivot"
        :widget-language="topBrands.language_dim_pivot"
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
  name: 'TopBrandsSettingsModal',
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
    topBrands() {
      return this.widgets['top_10_brands_widget']
    },
  },
  methods: {
    ...mapActions([
      action.UPDATE_AVAILABLE_WIDGETS,
      action.GET_AVAILABLE_WIDGETS,
      action.GET_TOP_BRANDS_WIDGET,
    ]),
    async saveOptions() {
      await this[action.UPDATE_AVAILABLE_WIDGETS]({
        projectId: this.projectId,
        data: {
          top_10_brands_widget: {
            id: this.topBrands.id,
            title: this.title || this.topBrands.title,
            description: this.description || this.topBrands.description,
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
          top_10_brands_widget: {
            id: this.topBrands.id,
            title: title || this.topBrands.title,
            description: description || this.topBrands.description,
            smpl_freq:
              aggregationPeriod.toLowerCase() || this.topBrands.smpl_freq,
          },
        },
      })
      await this[action.GET_TOP_BRANDS_WIDGET](this.projectId)
      await this[action.GET_AVAILABLE_WIDGETS](this.projectId)
      this.$emit('close')
    },
    async saveDimensions(author, language, country) {
      if (author || author === '') {
        author = author || this.topBrands.author_dim_pivot
      }
      if (language || language === '') {
        language = language || this.topBrands.language_dim_pivot
      }
      if (country || country === '') {
        country = country || this.topBrands.country_dim_pivot
      }

      await this[action.UPDATE_AVAILABLE_WIDGETS]({
        projectId: this.projectId,
        data: {
          top_10_brands_widget: {
            id: this.topBrands.id,
            smpl_freq: this.topBrands.aggregation_period,
            author_dim_pivot: author,
            language_dim_pivot: language,
            country_dim_pivot: country,
            sentiment_dim_pivot: this.topBrands.sentiment_dim_pivot,
            source_dim_pivot: this.topBrands.source_dim_pivot,
          },
        },
      })

      this.loading = true
      await this[action.GET_AVAILABLE_WIDGETS](this.projectId)
      await this[action.GET_TOP_BRANDS_WIDGET](this.projectId)
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
