<template>
  <Choropleth :data="chartData" :options="chartOptions" />
</template>

<script>
import {createTypedChart} from 'vue-chartjs'
import {Chart, Tooltip} from 'chart.js'
import {
  ChoroplethController,
  GeoFeature,
  ColorScale,
  ProjectionScale,
} from 'chartjs-chart-geo'

Chart.register(
  ChoroplethController,
  GeoFeature,
  ColorScale,
  ProjectionScale,
  Tooltip
)

const Choropleth = createTypedChart('choropleth', 'choropleth')

import {topojson} from 'chartjs-chart-geo'
import countriesTopoJson from '@lib/countries-50m.json'

const countries = topojson
  .feature(countriesTopoJson, countriesTopoJson.objects.countries)
  .features.filter((f) => f.properties.name !== 'Antarctica')

export default {
  name: 'WorldMapChart',
  extends: Choropleth,
  components: {Choropleth},
  props: {
    chartValues: {type: Array, default: () => []},
    data: {type: Object, default: () => {}},
    options: {type: Object, default: () => {}},
  },
  computed: {
    chartData() {
      return {
        labels: countries.map((d) => d.properties.name),
        datasets: [
          {
            label: 'Countries',
            borderColor: '#B0B5B8',
            backgroundColor: (context) => {
              if (context.dataIndex == null) {
                return null
              }
              const value = context.dataset.data[context.dataIndex]
              return `rgb(81, 107, 238, ${this.opacity(value)})`
            },
            data: countries.map((d) => ({
              feature: d,
              value: this.getCountryValue(d),
            })),
          },
        ],
      }
    },
    chartOptions() {
      return {
        onClick: (e, dataOptions) => {
          this.$emit(
            'open-interactive-data',
            this.chartData.labels[dataOptions[0].index]
          )
        },
        showOutline: false,
        showGraticule: false,
        plugins: {
          legend: {
            display: false,
          },
          datalabels: {
            display: false,
          },
        },
        scales: {
          projection: {
            axis: 'x',
            projection: 'naturalEarth1',
          },
          color: {
            axis: 'x',
            display: false,
          },
        },
      }
    },
  },
  methods: {
    getCountryValue(countryData) {
      const existingСountry = this.chartValues.find(
        (el) => el.country === countryData.properties.name
      )?.count

      return existingСountry || '0'
    },
    opacity(countryData) {
      if (!+countryData.value) return '0'

      const length = this.chartValues.length
      const index = this.chartValues.findIndex(
        (el) => el.country === countryData.feature.properties.name
      )

      return (length - index) / length
    },
  },
}
</script>
