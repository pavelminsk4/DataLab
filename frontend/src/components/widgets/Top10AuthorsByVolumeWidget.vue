<template>
  <WidgetsLayout v-if="topAuthors" title="Top 10 authors by volume">
    <ChartsView
      :is-doughnut="true"
      :chart-data="chartData"
      :chart-options="chartOptions"
    />
  </WidgetsLayout>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'

import WidgetsLayout from '@/components/layout/WidgetsLayout'
import ChartsView from '@/components/widgets/charts/ChartsView'

export default {
  name: 'Top10AuthorsByVolumeWidget',
  components: {ChartsView, WidgetsLayout},
  props: {
    projectId: {
      type: Number,
      required: true,
    },
  },
  created() {
    this[action.GET_TOP_AUTHORS_WIDGET](this.projectId)
  },
  computed: {
    ...mapGetters({
      topAuthors: get.TOP_AUTHORS,
    }),
    value() {
      return this.topAuthors.map((el) => el.author_posts_count)
    },
    labels() {
      return this.topAuthors.map((el) => el.entry_author)
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
            cutout: 160,
            radius: 100,
            borderColor: 'transparent',
            borderRadius: 30,
            spacing: 5,
            data: this.value,
          },
        ],
      }
    },
    chartOptions() {
      return {
        plugins: {
          legend: {
            position: 'left',
            labels: {
              boxWidth: 5,
            },
          },
        },
        responsive: true,
        maintainAspectRatio: false,
      }
    },
  },
  methods: {
    ...mapActions([action.GET_TOP_AUTHORS_WIDGET]),
  },
}
</script>

<style scoped></style>
