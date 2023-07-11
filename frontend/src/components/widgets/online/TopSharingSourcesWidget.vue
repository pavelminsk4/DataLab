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
        :source-name="item.url"
        :value="item.value"
        :widget-details="widgetDetails"
      >
        <template #sentimentBar v-if="checkSentimentData(item.sentiments)">
          <span class="chart-title">Sentiment</span>
          <ChartsView
            :widget-details="widgetDetails"
            :chart-values="datasets(item)"
            :iteractiveLabel="item.name"
            chart-type="StackedBarChart"
          />
        </template>
      </SharingSourcesCard>
    </div>
  </component>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import {get, action} from '@store/constants'
import {capitalizeFirstLetter} from '@/lib/utilities'

import ChartsView from '@/components/charts/ChartsView'
import WidgetsLayout from '@/components/layout/WidgetsLayout'
import SharingSourcesCard from '@/components/widgets/SharingSourcesCard'

export default {
  name: 'TopSharingSourcesWidget',
  components: {
    WidgetsLayout,
    SharingSourcesCard,
    ChartsView,
  },
  props: {
    widgetDetails: {type: Object, required: true},
    isSettings: {type: Boolean, default: false},
  },
  computed: {
    ...mapGetters({
      topSharingSources: get.TOP_SHARING_SOURCES,
    }),
    widgetWrapper() {
      return this.isSettings ? 'div' : 'WidgetsLayout'
    },
  },
  created() {
    if (!this.topSharingSources.length) {
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
          data: [item.sentiments[key] * barPercent],
          backgroundColor: colors[key],
          borderRadius: 12,
          label: key,
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
</style>
