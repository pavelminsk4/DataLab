<template>
  <WidgetsLayout
    v-if="topAuthors"
    :title="widgets['top_10_authors_by_volume_widget'].title"
    @delete-widget="$emit('delete-widget')"
    @open-modal="$emit('open-summary-modal')"
  >
    <div class="top-authors-wrapper">
      <div class="legend-box">
        <table class="general-legend">
          <td
            v-for="(item, index) in topAuthorsVolume.slice(0, 2)"
            :key="item.entry_author + index"
            @click="toggleData($event.target, item)"
            @mouseover="handleHover($event, item)"
            @mouseleave="handleLeave"
            class="legend"
          >
            <span :style="`color: ${item.color}`" class="legend-percent">
              {{ percentageIndicator(item.author_posts_count) }}
            </span>
            {{ item.entry_author }}
          </td>
          <td
            v-for="(item, index) in topAuthorsVolume.slice(2, 4)"
            :key="item.entry_author + index"
            @click="toggleData($event.target, item)"
            @mouseover="handleHover($event, item)"
            @mouseleave="handleLeave"
            class="legend"
          >
            <span
              :style="`color: ${item.color}; font-size: 18px; white-space: nowrap;`"
              class="legend-percent"
            >
              {{ percentageIndicator(item.author_posts_count) }}
            </span>
            {{ item.entry_author }}
          </td>
        </table>
        <table class="secondary-legend">
          <td
            v-for="(item, index) in topAuthorsVolume.slice(4, 7)"
            :key="item.entry_author + index"
            @click="toggleData($event.target, item)"
            @mouseover="handleHover($event, item)"
            @mouseleave="handleLeave"
            class="min-legend"
          >
            <span
              :style="`color: ${item.color}; font-size: 18px; white-space: nowrap;`"
              class="legend-percent"
            >
              {{ percentageIndicator(item.author_posts_count) }}
            </span>
            {{ item.entry_author }}
          </td>
        </table>
        <table class="secondary-legend">
          <td
            v-for="(item, index) in topAuthorsVolume.slice(7, 9)"
            :key="item.entry_author + index"
            @click="toggleData($event.target, item)"
            @mouseover="handleHover($event, item)"
            @mouseleave="handleLeave"
            class="min-legend"
          >
            <span
              :style="`color: ${item.color}; font-size: 18px; white-space: nowrap;`"
              class="legend-percent"
            >
              {{ percentageIndicator(item.author_posts_count) }}
            </span>
            {{ item.entry_author }}
          </td>
        </table>
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
  name: 'Top10AuthorsByVolumeWidget',
  components: {WidgetsLayout, Doughnut},
  props: {
    projectId: {
      type: Number,
      required: true,
    },
  },
  data() {
    return {
      percent: '',
      text: '',
      count: '',
    }
  },
  created() {
    this[action.GET_TOP_AUTHORS_WIDGET](this.projectId)
  },
  computed: {
    ...mapGetters({
      topAuthors: get.TOP_AUTHORS,
      widgets: get.AVAILABLE_WIDGETS,
    }),
    value() {
      return this.topAuthors.map((el) => el.author_posts_count)
    },
    labels() {
      return this.topAuthors.map((el) => el.entry_author)
    },
    topAuthorsVolume() {
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
      const topAuthorsWithColors = []
      this.topAuthors.map((el, index) =>
        topAuthorsWithColors.push({...el, color: backgroundColors[index]})
      )
      return topAuthorsWithColors
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
    ...mapActions([action.GET_TOP_AUTHORS_WIDGET]),
    percentageIndicator(val) {
      let sum = this.value.reduce(
        (accumulator, currentValue) => accumulator + currentValue
      )
      return ((100 * val) / sum).toFixed(2).toString() + ' %'
    },
    handleHover(evt, item) {
      const indexItem = this.topAuthorsVolume.indexOf(item)
      this.percent = this.percentageIndicator(item.author_posts_count)
      this.text = item.entry_author
      this.count = item.author_posts_count
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
    toggleData(button, item) {
      const index = this.topAuthorsVolume.indexOf(item)
      this.$refs.doughnut.chart.toggleDataVisibility(index)
      this.$refs.doughnut.chart.update()
      if (this.$refs.doughnut.chart.getDataVisibility(index)) {
        button.classList.remove('hidden')
      } else {
        button.classList.add('hidden')
      }
    },
  },
}
</script>

<style lang="scss" scoped>
.hidden {
  text-decoration: line-through;
}

.top-authors-wrapper {
  position: relative;

  display: flex;
  justify-content: center;
  gap: 50px;

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
.doughnut-wrapper {
  position: relative;

  display: flex;
  align-items: center;
  justify-content: center;

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
  overflow-y: hidden;
  overflow-x: auto;
  height: 100%;

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
</style>

<style>
#doughnut-chart {
  height: 320px;
  width: 275px;
}
</style>
