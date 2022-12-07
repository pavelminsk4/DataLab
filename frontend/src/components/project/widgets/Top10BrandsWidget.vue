<template>
  <WidgetsLayout
    v-if="topBrands"
    :title="widgets['top_10_brands_widget'].title"
    @delete-widget="$emit('delete-widget')"
    @open-modal="$emit('open-settings-modal')"
  >
    <div class="top-authors-wrapper">
      <div class="legends">
        <div class="legend-wrapper">
          <div
            v-for="(item, index) in topBrandsVolume.slice(0, 4)"
            :key="item.feedlink__source1 + index"
            :id="getId(item)"
            @click="toggleData($event.target, item, getId(item))"
            @mouseover="handleHover($event, item)"
            @mouseleave="handleLeave"
            class="legend-item"
          >
            <div
              :style="`color: ${item.color}; font-size: 18px; white-space: nowrap;`"
              class="legend-percent"
            >
              {{ percentageIndicator(item.brand_count) }}
            </div>
            <div class="author">{{ item.feedlink__source1 }}</div>
          </div>
        </div>

        <div class="legends-additional-wrapper">
          <div
            v-for="(item, index) in topBrandsVolume.slice(4, 10)"
            :key="item.feedlink__source1 + index"
            :id="getId(item)"
            @click="toggleData($event.target, item, getId(item))"
            @mouseover="handleHover($event, item)"
            @mouseleave="handleLeave"
            class="legend-item"
          >
            <div
              :style="`color: ${item.color}; font-size: 14px; white-space: nowrap; font-weight: 600;`"
              class="legend-percent"
            >
              {{ percentageIndicator(item.brand_count) }}
            </div>
            <div class="author">{{ item.feedlink__source1 }}</div>
          </div>
        </div>
      </div>

      <div class="doughnut-wrapper">
        <Doughnut
          :chart-options="chartOptions"
          :chart-data="chartData"
          ref="doughnut"
          class="doughnut-chart-widget"
        />

        <div class="circle-wrapper">
          <div class="percent">{{ percent }}</div>
          <div class="text">{{ text }}</div>
          <div :class="[count && 'count']">{{ count }}</div>
        </div>
      </div>
    </div>
  </WidgetsLayout>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'
import {Doughnut} from 'vue-chartjs'

import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  ArcElement,
  CategoryScale,
} from 'chart.js'

ChartJS.register(Title, Tooltip, Legend, ArcElement, CategoryScale)

import WidgetsLayout from '@/components/layout/WidgetsLayout'
export default {
  name: 'Top10BrandsWidget',
  components: {WidgetsLayout, Doughnut},
  props: {
    projectId: {
      type: Number,
      required: true,
    },
  },
  created() {
    if (!this.topBrands.length) {
      this[action.GET_TOP_BRANDS_WIDGET](this.projectId)
    }
  },
  computed: {
    ...mapGetters({
      topBrands: get.TOP_BRANDS,
      widgets: get.AVAILABLE_WIDGETS,
    }),
    value() {
      return this.topBrands.map((el) => el.brand_count)
    },
    labels() {
      return this.topBrands.map((el) => el.feedlink__source1)
    },
    topBrandsVolume() {
      const backgroundColors = [
        '#055FFC',
        '#7A9EF9',
        '#47F9B9',
        '#47F979',
        '#95F947',
        '#F5F947',
        '#F6AA37',
        '#F63737',
        '#F63787',
        '#D930F4',
      ]
      const topBrandsWithColors = []
      this.topBrands.map((el, index) =>
        topBrandsWithColors.push({...el, color: backgroundColors[index]})
      )
      return topBrandsWithColors
    },
    chartData() {
      return {
        labels: this.labels,
        datasets: [
          {
            backgroundColor: [
              '#055FFC',
              '#7A9EF9',
              '#47F9B9',
              '#47F979',
              '#95F947',
              '#F5F947',
              '#F6AA37',
              '#F63737',
              '#F63787',
              '#D930F4',
            ],
            hoverOffset: 5,
            radius: 100,
            borderColor: 'transparent',
            borderRadius: 30,
            spacing: 5,
            cutout: '85%',
            data: this.value,
          },
        ],
      }
    },
    chartOptions() {
      return {
        plugins: {
          legend: false,
        },
        responsive: true,
        maintainAspectRatio: false,
      }
    },
  },
  methods: {
    ...mapActions([action.GET_TOP_BRANDS_WIDGET]),
    percentageIndicator(val) {
      let sum = this.value.reduce(
        (accumulator, currentValue) => accumulator + currentValue
      )
      return ((100 * val) / sum).toFixed(2).toString() + ' %'
    },
    handleHover(evt, item) {
      const indexItem = this.topBrandsVolume.indexOf(item)
      this.percent = this.percentageIndicator(item.brand_count)
      this.text = item.feedlink__source1
      this.count = item.brand_count
      this.$refs.doughnut.chart.data.datasets[0].backgroundColor.forEach(
        (color, index, colors) => {
          colors[index] =
            index === indexItem || color.length === 9 ? color : color + '4D'
        }
      )
      this.$refs.doughnut.chart.update()
    },
    handleLeave() {
      this.percent = ''
      this.text = ''
      this.count = ''
      this.$refs.doughnut.chart.data.datasets[0].backgroundColor.forEach(
        (color, index, colors) => {
          colors[index] = color.length === 9 ? color.slice(0, -2) : color
        }
      )
      this.$refs.doughnut.chart.update()
    },
    toggleData(button, item, id) {
      const element = document.getElementById(id)

      const index = this.topBrandsVolume.indexOf(item)
      this.$refs.doughnut.chart.toggleDataVisibility(index)
      this.$refs.doughnut.chart.update()
      if (
        this.$refs.doughnut.chart.getDataVisibility(index) &&
        !Array.from(element).find((el) => el.contains(event.target))
      ) {
        element.classList.remove('hidden')
      } else {
        element.classList.add('hidden')
      }
    },
    getId(item) {
      return this.topBrandsVolume.indexOf(item)
    },
  },
}
</script>

<style lang="scss" scoped>
.top-authors-wrapper {
  display: grid;
  grid-template-columns: 50% 50%;
  align-items: center;

  min-width: 100%;
  margin-left: 12px;

  overflow-y: hidden;

  .legend-box {
    display: flex;
    flex-direction: column;

    width: 300px;
    margin-top: 30px;

    .general-legend {
      display: flex;
      flex-wrap: wrap;

      width: 400px;

      .legend {
        display: flex;
        gap: 16px;

        width: 180px;
        margin-bottom: 6px;

        font-style: normal;
        font-weight: 400;
        font-size: 14px;
        line-height: 25px;
        color: var(--primary-text-color);

        &:last-child {
          margin-left: 30px;
        }

        &:first-child {
          margin-right: 30px;
        }

        .legend-percent {
          white-space: nowrap;

          cursor: pointer;

          font-weight: 600;
          font-size: 18px;
          line-height: 25px;
        }
      }
    }

    .secondary-legend {
      display: flex;
      justify-content: space-between;

      width: 350px;
      margin-top: 28px;

      .min-legend {
        display: flex;
        flex-direction: column;

        max-width: 65px;
        overflow: hidden;
        text-overflow: ellipsis;

        font-style: normal;
        font-weight: 400;
        font-size: 12px;
        line-height: 20px;
        color: var(--primary-text-color);
      }
    }

    &::-webkit-scrollbar {
      height: 5px;
      width: 5px;
    }

    &::-webkit-scrollbar-track {
      background: var(--secondary-bg-color);
      border: 1px solid var(--input-border-color);
      border-radius: 0 10px 10px 0;
    }

    &::-webkit-scrollbar-thumb {
      height: 4px;

      background: var(--secondary-text-color);
      border-radius: 10px;
    }
  }
}
.legends {
  display: flex;
  flex-direction: column;

  width: fit-content;

  overflow: hidden;
  z-index: 2;

  .legend-wrapper {
    display: grid;
    grid-template-columns: 160px 160px;
    grid-template-rows: auto auto;

    margin: 0 0 20px;

    .legend-item {
      display: grid;
      grid-template-columns: 75px auto;

      min-height: 40px;
      margin-right: 10px;

      cursor: pointer;

      font-size: 14px;

      .author {
        display: block;

        text-overflow: ellipsis;
        white-space: nowrap;
        overflow: hidden;
      }

      &:hover {
        .author {
          white-space: normal;
          overflow: revert;
          word-break: break-all;
        }
      }
    }
  }

  .legends-additional-wrapper {
    display: grid;
    grid-template-columns: 110px 110px 110px;
    grid-template-rows: auto auto;

    .legend-item {
      display: grid;
      grid-template-rows: 22px auto;

      margin: 0 5px 5px 0;

      cursor: pointer;

      font-style: normal;
      font-weight: 400;
      font-size: 12px;
      line-height: 20px;

      .author {
        display: block;

        text-overflow: ellipsis;
        white-space: nowrap;
        overflow: hidden;
      }

      &:hover {
        .author {
          white-space: normal;
          overflow: revert;
        }
      }

      .legend-percent {
        font-style: normal;
        font-weight: 400;
        font-size: 12px;
        line-height: 20px;
      }
    }
  }
}

.doughnut-wrapper {
  position: relative;

  display: flex;
  align-items: center;
  justify-content: center;

  width: fit-content;

  z-index: 1;

  .circle-wrapper {
    position: absolute;

    display: flex;
    flex-direction: column;
    align-items: center;

    .percent {
      margin-bottom: 10px;

      font-style: normal;
      font-weight: 600;
      font-size: 22px;
      line-height: 25px;
    }

    .text {
      max-width: 50px;
      overflow: hidden;
      text-overflow: ellipsis;
      white-space: nowrap;

      margin-bottom: 20px;

      text-align: center;

      font-style: normal;
      font-weight: 400;
      font-size: 12px;
      line-height: 14px;
    }

    .count {
      padding: 2px 10px;

      border-radius: 29px;
      background-color: rgba(255, 255, 255, 0.2);

      font-style: normal;
      font-weight: 500;
      font-size: 12px;
      line-height: 20px;
    }
  }
}

.top-authors-wrapper {
  width: fit-content;

  &::-webkit-scrollbar {
    height: 5px;
    width: 5px;
  }

  &::-webkit-scrollbar-track {
    background: var(--secondary-bg-color);
    border: 1px solid var(--input-border-color);
    border-radius: 0 10px 10px 0;
  }

  &::-webkit-scrollbar-thumb {
    height: 4px;

    background: var(--secondary-text-color);
    border-radius: 10px;
  }
}

@media screen and (min-width: 1400px) {
  .top-authors-wrapper {
    overflow: hidden;
  }
}
</style>
