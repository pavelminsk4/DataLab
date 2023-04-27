import {mapActions} from 'vuex'
import {action} from '@store/constants'

import ButtonWithArrow from '@/components/common/ButtonWithArrow'

export default {
  components: {ButtonWithArrow},
  computed: {
    routeName() {
      return this.$route.name
    },
  },
  methods: {
    ...mapActions([action.UPDATE_NEW_WORKSPACE]),
    getNextStepName(nextStep) {
      return this.routeName.replace(/\d/g, nextStep)
    },
  },
}
