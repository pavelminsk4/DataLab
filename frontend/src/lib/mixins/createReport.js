import {mapActions} from 'vuex'
import {action} from '@store/constants'

export default {
  computed: {
    routeName() {
      return this.$route.name
    },
  },
  methods: {
    ...mapActions([action.UPDATE_NEW_REPORT]),
    getNextStepName(nextStep) {
      return this.routeName.replace(/\d/g, nextStep)
    },
  },
}
