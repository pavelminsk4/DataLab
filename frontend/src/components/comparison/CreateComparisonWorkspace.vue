<template>
  <div class="form-wrapper">
    <BaseInput v-model="workspaceName" label="Name" class="input-name" />

    <BaseTextarea
      v-model="workspaceDescription"
      placeholder="Some words about workspace"
      label="Description"
    />

    <footer class="create-workspace__footer">
      <ButtonWithArrow :is-disabled="!workspaceName" @click="nextStep">
        <CustomText tag="span" text="Next" />
      </ButtonWithArrow>
    </footer>
  </div>
</template>

<script>
import {mapActions, mapGetters, mapState} from 'vuex'
import {action, get} from '@store/constants'
import ComparisonMixin from '@lib/mixins/comparison.js'

import CustomText from '@components/CustomText'

export default {
  name: 'CreateComparisonWorkspace',
  components: {CustomText},
  mixins: [ComparisonMixin],
  data() {
    return {
      workspaceName: '',
      workspaceDescription: '',
    }
  },
  computed: {
    ...mapState(['userInfo']),
    ...mapGetters({
      department: get.DEPARTMENT,
    }),
  },
  created() {
    this[action.CLEAR_STATE]()
    this[action.GET_COMPANY_USERS](this.department.id)
  },
  methods: {
    ...mapActions([action.GET_COMPANY_USERS, action.CLEAR_STATE]),
    nextStep() {
      const nextStep = 2
      const nextStepName = this.getNextStepName(nextStep)

      this[action.UPDATE_NEW_COMPARISON_WORKSPACE]({
        step: nextStep,
        title: this.workspaceName,
        description: this.workspaceDescription,
        department: this.department.id,
        members: [this.userInfo.id],
      })
      this.$router.push({name: nextStepName})
    },
  },
}
</script>

<style lang="scss" scoped>
.form-wrapper {
  display: flex;
  flex-direction: column;

  width: 75%;
  margin-top: 40px;
  gap: 25px;
}

.create-workspace__footer {
  display: flex;
  justify-content: flex-end;
}
</style>
