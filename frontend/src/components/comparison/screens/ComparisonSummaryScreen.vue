<template>
  <div>Features Screen</div>
</template>

<script>
import {createNamespacedHelpers} from 'vuex'
import {action} from '@store/constants'

const {mapActions, mapState} = createNamespacedHelpers('comparison/widgets')

export default {
  name: 'ComparisonSummaryScreen',
  props: {
    currentProject: {type: Object, required: true},
  },
  computed: {
    ...mapState(['summary']),
  },
  created() {
    if (!this.summary.length)
      this[action.GET_SUMMARY_WIDGETS](this.currentProject.id)
  },
  methods: {
    ...mapActions([action.GET_SUMMARY_WIDGETS]),
  },
}
</script>

<style lang="scss" scoped></style>
