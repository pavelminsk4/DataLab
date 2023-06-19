<template>
  <div>Languages By Country</div>
</template>

<script>
import {mapActions, mapState} from 'vuex'
import {action} from '@store/constants'

export default {
  name: 'LanguagesByCountryWidget',
  props: {
    widgetDetails: {type: Object, required: true},
  },
  computed: {
    ...mapState(['languagesByCountry']),
    chartData() {
      console.log(this.languagesByCountry)
      return true
    },
  },
  created() {
    if (!this.languagesByCountry.length) {
      this[action.GET_LANGUAGES_BY_COUNTRY]({
        projectId: this.widgetDetails.projectId,
        widgetId: this.widgetDetails.id,
      })
    }
  },
  methods: {
    ...mapActions([action.GET_LANGUAGES_BY_COUNTRY]),
  },
}
</script>
