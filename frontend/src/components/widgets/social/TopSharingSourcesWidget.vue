<template>
  <component
    :is="widgetWrapper"
    :widget-id="widgetDetails.id"
    :title="widgetDetails.title"
    style="--widget-layout-content-padding: 0px"
    @delete-widget="$emit('delete-widget')"
    @open-modal="$emit('open-settings-modal')"
  >
    <div class="sharing-sources-wrapper">
      <SharingSourcesCard
        v-for="(item, index) in topSharingSources"
        :key="'source' + index"
        :type="item.type"
        :img="item.picture"
        :name="item.name"
        :source-name="`@${item.alias}`"
        :value="item.value"
        :widget-details="widgetDetails"
      >
        <template #chips>
          <div class="type">
            <component
              :is="capitalizeFirstLetter(item.source) + 'Icon'"
              :class="item.source"
            />
            <CustomText tag="span" :text="item.source" />
          </div>
          <BaseChips :chips-type="item.gender" />
        </template>

        <template #sentimentBar v-if="checkSentimentData(item.sentiments)">
          <CustomText tag="span" text="Sentiment" class="chart-title" />
          <ChartsView
            :widget-details="widgetDetails"
            :chart-values="datasets(item)"
            :iteractiveLabel="item.alias"
            chart-type="StackedBarChart"
          />
        </template>
      </SharingSourcesCard>
    </div>
  </component>
</template>

<script>
import {createNamespacedHelpers} from 'vuex'
import {get, action} from '@store/constants'
import {capitalizeFirstLetter} from '@/lib/utilities'

import CustomText from '@/components/CustomText'
import BaseChips from '@/components/BaseChips'
import TwitterIcon from '@/components/icons/TwitterIcon'
import ChartsView from '@/components/charts/ChartsView'
import WidgetsLayout from '@/components/layout/WidgetsLayout'
import SharingSourcesCard from '@/components/widgets/SharingSourcesCard'

const {mapActions, mapGetters} = createNamespacedHelpers('social/widgets')

export default {
  name: 'TopSharingSourcesWidget',
  components: {
    WidgetsLayout,
    SharingSourcesCard,
    TwitterIcon,
    ChartsView,
    BaseChips,
    CustomText,
  },
  props: {
    widgetDetails: {type: Object, required: true},
    isSettings: {type: Boolean, default: false},
  },
  computed: {
    ...mapGetters({
      socialWidgets: get.SOCIAL_WIDGETS,
    }),
    topSharingSources() {
      return (
        this.widgetDetails.widgetData || this.socialWidgets.topSharingSources
      )
    },
    widgetWrapper() {
      return this.isSettings ? 'div' : 'WidgetsLayout'
    },
  },
  created() {
    if (!this.widgetDetails.widgetData && !this.topSharingSources.length) {
      this[action.GET_TOP_SHARING_SOURCES]({
        projectId: this.widgetDetails.projectId,
        widgetId: this.widgetDetails.id,
      })
    }
  },
  methods: {
    ...mapActions([action.GET_TOP_SHARING_SOURCES]),
    capitalizeFirstLetter,
    datasets(item) {
      const barPercent =
        Object.values(item.sentiments).reduce((a, b) => a + b, 0) /
        Object.values(item.sentiments).length

      const colors = {
        positive: '#00b884',
        negative: '#ed2549',
        neutral: '#516bee',
      }

      return Object.keys(item.sentiments).map((key) => {
        return {
          label: key,
          data: [item.sentiments[key] * barPercent],
          backgroundColor: colors[key],
          borderRadius: 12,
        }
      })
    },
    checkSentimentData(sentiments) {
      return !!Object.values(sentiments).filter((sentiment) => sentiment).length
    },
  },
}
</script>

<style scoped>
.sharing-sources-wrapper {
  display: flex;
  gap: 12px;
  padding: 15px;
  height: 100%;
}

.type {
  display: flex;

  align-items: center;
  gap: 4px;

  padding: 6px 8px;

  background: var(--chips-background-secondary-color);
  border-radius: 2px 12px 12px 2px;

  font-style: normal;
  font-weight: 400;
  font-size: 12px;
  line-height: 16px;
  color: var(--typography-primary-color);
}

.male {
  background-color: var(--male-bg-color);
}

.female {
  background-color: var(--female-bg-color);
}

.twitter {
  height: 26px;
  width: 26px;
  padding: 4px;

  border-radius: 4px;

  color: var(--button-text-color);
}
</style>
