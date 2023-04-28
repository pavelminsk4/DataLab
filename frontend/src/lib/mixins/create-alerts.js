import {createNamespacedHelpers} from 'vuex'
import {action} from '@store/constants'

import ButtonWithArrow from '@/components/common/ButtonWithArrow'

const {mapActions: mapActionsAlerts} = createNamespacedHelpers('alerts')

export default {
  components: {ButtonWithArrow},
  computed: {
    routeName() {
      return this.$route.name
    },
  },
  methods: {
    ...mapActionsAlerts([action.UPDATE_NEW_ALERT]),
    getNextStepName(nextStep) {
      return this.routeName.replace(/\d/g, nextStep)
    },
  },
}
