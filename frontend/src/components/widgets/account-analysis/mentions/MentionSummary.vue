<template>
  <AccountAnalysisSummaryWidget
    :widget-data="mentionSummary"
    :stats="statistiscs"
  />
</template>

<script>
import {createNamespacedHelpers} from 'vuex'
import {get, action} from '@store/constants'

import AccountAnalysisSummaryWidget from '@components/widgets/AccountAnalysisSummaryWidget'

import {isAllFieldsEmpty} from '@lib/utilities'

const {mapActions, mapGetters} = createNamespacedHelpers(
  'accountAnalysis/widgets'
)

export default {
  name: 'MentionSummary',
  components: {AccountAnalysisSummaryWidget},
  props: {
    widgetDetails: {type: Object, required: true},
  },
  computed: {
    ...mapGetters({
      accountAnalysisWidgets: get.ACCOUNT_ANALYSIS_WIDGETS,
    }),
    mentionSummary() {
      return this.accountAnalysisWidgets.mentionSummary
    },
    statistiscs() {
      const {stats} = this.mentionSummary
      if (isAllFieldsEmpty(stats)) return []
      return [
        {
          name: 'Total mention number',
          value: stats.mention,
          iconName: 'NewPost',
        },
        {
          name: 'Language number',
          value: stats.language,
          iconName: 'LanguageSymbols',
        },
        {
          name: 'Countries number',
          value: stats.countries,
          iconName: 'Country',
        },
        {
          name: 'Authors number',
          value: stats.authors,
          iconName: 'Author',
        },
        {name: 'Neutral mention', value: stats.neutral, iconName: 'Neutral'},
        {name: 'Negative mention', value: stats.negative, iconName: 'Negative'},
        {name: 'Positive mention', value: stats.positive, iconName: 'Positive'},
        {
          name: 'Potential rates',
          value: stats.potential_rates,
          iconName: 'Graph',
        },
      ]
    },
  },
  created() {
    if (!this.mentionSummary.length) {
      this[action.GET_MENTION_SUMMARY]({
        projectId: this.widgetDetails.projectId,
        widgetId: this.widgetDetails.id,
        value: this.widgetDetails.aggregation_period,
      })
    }
  },
  methods: {
    ...mapActions([action.GET_MENTION_SUMMARY]),
  },
}
</script>

<style lang="scss" scoped></style>
