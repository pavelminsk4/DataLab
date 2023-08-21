<template>
  <div class="form-wrapper">
    <BaseInput
      v-model="projectName"
      label="Name"
      placeholder="Project Name"
      class="input-name-field"
    />

    <BaseTextarea
      v-model="projectDescription"
      placeholder="Some words about your project"
      label="Description"
      class="input-name-field"
    />

    <footer class="create-project__footer">
      <ButtonWithArrow
        :is-disabled="!projectName"
        class="button"
        @click="nextStep"
      >
        <CustomText tag="span" text="Next" />
      </ButtonWithArrow>
    </footer>
  </div>
</template>

<script>
import {mapActions, mapState} from 'vuex'
import {action} from '@store/constants'
import TFSMixin from '@/lib/mixins/twenty-four-seven.js'

import CustomText from '@/components/CustomText'
import BaseInput from '@/components/common/BaseInput'
import BaseTextarea from '@/components/common/BaseTextarea'
import ButtonWithArrow from '@/components/common/ButtonWithArrow'

export default {
  name: 'CreateTFSProject',
  mixins: [TFSMixin],
  components: {
    CustomText,
    BaseInput,
    BaseTextarea,
    ButtonWithArrow,
  },
  props: {
    workspaceId: {type: String, default: null},
    moduleName: {type: String, default: ''},
  },
  data() {
    return {
      projectName: '',
      projectDescription: '',
    }
  },
  computed: {
    ...mapState(['userInfo']),
  },
  created() {
    if (this.workspaceId !== 'new' && this.currentStep === 'TFSWorkspaceStep2')
      this[action.CLEAR_STATE]()
  },
  methods: {
    ...mapActions([action.CLEAR_STATE, action.UPDATE_NEW_TFS_PROJECT]),

    nextStep() {
      const nextStep = 3
      const nextStepName = this.getNextStepName(nextStep)

      this[action.UPDATE_NEW_TFS_PROJECT]({
        step: nextStepName,
        creator: this.userInfo.id,
        members: [this.userInfo.id],
        title: this.projectName,
        description: this.projectDescription,
        source: this.moduleName,
        workspace: +this.workspaceId ? this.workspaceId : null,
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

  width: 90%;
  margin-top: 40px;

  .input-name-field {
    max-width: 408px;
    margin-bottom: 32px;
  }

  .create-project__footer {
    display: flex;
    justify-content: flex-end;

    max-width: 408px;
  }
}
</style>
