<template>
  <MainLayoutTitleBlock
    title="Reports"
    description="Set up and manage reports"
    :back-page="{
      name: 'main page',
      routName: 'MainView',
    }"
  />

  <ReportProgressBar />

  <div class="form-wrapper">
    <BaseInput v-model="reportName" label="Name" class="input-name" />

    <BaseTextarea
      v-model="reportDescription"
      placeholder="Some words about Workspace"
      label="Description"
    />

    <BaseButton
      :is-disabled="!reportName"
      class="next-button"
      @click="nextStep"
    >
      <span>Next</span>
      <ArrowLeftIcon class="button-arrow-icon" />
    </BaseButton>
  </div>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'

import ArrowLeftIcon from '@/components/icons/ArrowLeftIcon'
import BaseButton from '@/components/common/BaseButton'
import BaseInput from '@/components/common/BaseInput'
import BaseTextarea from '@/components/common/BaseTextarea'
import MainLayoutTitleBlock from '@components/layout/MainLayoutTitleBlock'
import ReportProgressBar from '@/components/reports/ReportProgressBar'

export default {
  name: 'CreateWorkspaceScreen',
  components: {
    ArrowLeftIcon,
    BaseButton,
    BaseInput,
    BaseTextarea,
    MainLayoutTitleBlock,
    ReportProgressBar,
  },
  data() {
    return {
      reportName: '',
      reportDescription: '',
    }
  },
  computed: {
    ...mapGetters({
      // change
      user: get.USER_INFO,
    }),
    members() {
      //change
      return [this.user.id]
    },
    routName() {
      return this.$route.name
    },
  },
  created() {
    this[action.CLEAR_NEW_REPORT]()
  },
  methods: {
    ...mapActions([action.UPDATE_NEW_REPORT, action.CLEAR_NEW_REPORT]),
    nextStep() {
      const nextStep = this.routName.replace(/\d/g, '2')
      try {
        this[action.UPDATE_NEW_REPORT]({
          step: 2,
          title: this.reportName,
          description: this.reportDescription,
          members: this.members,
          department: this.user.user_profile.department.id,
        })
        this.$router.push({name: nextStep})
      } catch (e) {
        console.log(e)
      }
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

.next-button {
  align-self: flex-end;

  margin-top: 32px;

  .button-arrow-icon {
    margin-left: 10px;
    transform: rotate(180deg);
  }
}
</style>
