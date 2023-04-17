import {mapActions, mapState} from 'vuex'
import {action} from '@store/constants'

import ButtonWithArrow from '@/components/common/ButtonWithArrow'

export default {
  components: {ButtonWithArrow},
  computed: {
    ...mapState(['newReport']),
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
