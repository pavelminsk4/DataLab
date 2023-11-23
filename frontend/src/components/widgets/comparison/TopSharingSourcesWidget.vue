<template>
  <OverviewTopSharingSources
    :widget-details="widgetDetails"
    :widget-headers="widgetHeaders"
  />
</template>

<script>
import OverviewTopSharingSources from '@components/widgets/comparison/OverviewTopSharingSources'

export default {
  name: 'TopSharingSourcesWidget',
  components: {OverviewTopSharingSources},
  props: {
    widgetDetails: {type: Object, required: true},
  },
  created() {
    const tableHeaders = {
      social: [
        [
          {name: '', width: '5%'},
          {name: 'Project', width: '10%'},
          {
            name: 'Most active author',
            width: '15%',
            hasIcon: true,
            iconName: 'MostActiveAuthor',
          },
          {name: 'Gender', width: '15%'},
          {name: 'Media Type', width: '10%'},
          {name: 'Post', width: '10%'},
          {name: 'Sentiment', width: '35%'},
        ],
        [
          {name: '', width: '5%'},
          {name: 'Project', width: '10%'},
          {
            name: 'Most influential author',
            width: '15%',
            hasIcon: true,
            iconName: 'MostInfluentialAuthor',
          },
          {name: 'Gender', width: '15%'},
          {name: 'Media Type', width: '10%'},
          {
            name: 'Engagements',
            width: '10%',
          },
          {name: 'Sentiment', width: '35%'},
        ],
      ],
      online: [
        [
          {name: '', width: '5%'},
          {name: 'Project', width: '15%'},
          {name: 'Most active site', width: '20%'},
          {name: 'Post', width: '10%'},
          {name: 'Sentiment', width: '35%'},
        ],
        [
          {name: '', width: '5%'},
          {name: 'Project', width: '15%'},
          {name: 'Most influential site', width: '20%'},
          {
            name: 'Engagements',
            width: '10%',
          },
          {name: 'Sentiment', width: '35%'},
        ],
      ],
    }
    this.widgetHeaders = tableHeaders[`${this.widgetDetails.module}`]
  },
}
</script>
