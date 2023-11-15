import {createNamespacedHelpers} from 'vuex'
import {action} from '@store/constants'

import ButtonWithArrow from '@components/common/ButtonWithArrow'
import BaseInput from '@components/common/BaseInput'
import BaseTextarea from '@components/common/BaseTextarea'

const {mapActions} = createNamespacedHelpers('comparison')

export default {
  components: {ButtonWithArrow, BaseInput, BaseTextarea},
  computed: {
    routeName() {
      return this.$route.name
    },
  },
  methods: {
    ...mapActions([
      action.UPDATE_NEW_COMPARISON_WORKSPACE,
      action.UPDATE_NEW_COMPARISON_PROJECT,
    ]),
    getNextStepName(nextStep) {
      return this.routeName.replace(/\d/g, nextStep)
    },
  },
}
