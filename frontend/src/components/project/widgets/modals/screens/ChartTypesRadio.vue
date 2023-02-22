<template>
  <div class="chart-types">
    <BaseRadio
      v-for="(item, index) in availableTypes"
      :key="item + index"
      v-model="selectedValueProxy"
      :id="item + index"
      :value="item"
      :label="item"
      class="radio-button"
    />
  </div>
</template>

<script>
import {modalWidgetsConfig} from '@/lib/configs/widgetsConfigs'
import BaseRadio from '@/components/BaseRadio'
import {action} from '@store/constants'
import {mapActions} from 'vuex'

export default {
  name: 'ChartTypesRadio',
  components: {BaseRadio},
  props: {
    selected: {
      type: String,
      default: '',
    },
    widgetName: {
      type: String,
      required: false,
    },
    widgetData: {
      type: Object,
      default: () => {},
    },
    projectId: {
      type: Number,
      required: true,
    },
  },
  data() {
    return {
      selectedValue: '',
    }
  },
  computed: {
    availableTypes() {
      return modalWidgetsConfig[this.widgetName].availableTypes
    },
    selectedValueProxy: {
      get() {
        return this.selectedValue || this.selected
      },
      set(val) {
        this.selectedValue = val
        this.updateChartType()
      },
    },
  },
  methods: {
    ...mapActions([
      action.UPDATE_AVAILABLE_WIDGETS,
      action.GET_AVAILABLE_WIDGETS,
    ]),
    async updateChartType() {
      await this[action.UPDATE_AVAILABLE_WIDGETS]({
        projectId: this.projectId,
        data: {
          [this.widgetName]: {
            id: this.widgetData.id,
            chart_type: this.selectedValueProxy,
          },
        },
      })

      await this[action.GET_AVAILABLE_WIDGETS](this.projectId)
    },
  },
}
</script>

<style scoped>
.chart-types {
  margin-top: 20px;
}

.radio-button {
  margin: 12px 0;
}
</style>
