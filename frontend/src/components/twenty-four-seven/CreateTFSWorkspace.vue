<template>
  <div class="form-wrapper">
    <BaseInput v-model="workspaceName" label="Name" class="input-name" />

    <BaseTextarea
      v-model="workspaceDescription"
      placeholder="Some words about Workspace"
      label="Description"
    />

    <footer class="create-reports__footer">
      <ButtonWithArrow :is-disabled="!workspaceName" @click="nextStep">
        <CustomText tag="span" text="Next" />
      </ButtonWithArrow>
    </footer>
  </div>
</template>

<script>
import {mapActions, mapGetters, mapState} from 'vuex'
import {action, get} from '@store/constants'
import TFSMixin from '@lib/mixins/twenty-four-seven.js'

import CustomText from '@components/CustomText'
import BaseInput from '@components/common/BaseInput'
import BaseTextarea from '@components/common/BaseTextarea'
import ButtonWithArrow from '@components/common/ButtonWithArrow'

export default {
  name: 'CreateTFSWorkspace',
  mixins: [TFSMixin],
  components: {
    BaseInput,
    BaseTextarea,
    ButtonWithArrow,
    CustomText,
  },
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
    ...mapActions([
      action.GET_COMPANY_USERS,
      action.UPDATE_NEW_TFS_WORKSPACE,
      action.CLEAR_STATE,
    ]),
    nextStep() {
      const nextStep = 2
      const nextStepName = this.getNextStepName(nextStep)

      this[action.UPDATE_NEW_TFS_WORKSPACE]({
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

  width: 56%;
  margin-top: 40px;
}

.input-name {
  margin-bottom: 32px;
}

.report-add-users {
  width: 100%;
  margin-top: 32px;
}
</style>
