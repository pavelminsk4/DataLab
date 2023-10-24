<template>
  <div class="form-wrapper">
    <AccountAnalysisSourcesTabs class="tabs" />

    <BaseInput
      v-model="projectName"
      label="Name"
      placeholder="Project Name"
      class="input-name-field"
    />

    <CustomText text="Profile" class="title" />
    <BaseSearchField
      v-model="accountProfile"
      name="profile-handle-search"
      placeholder="Enter profile handle"
      :list="profileNames"
      :is-search="true"
      :current-value="accountProfile"
      :is-reject-selection="false"
      class="select-profile-handle"
      @select-option="selectProfile"
      @update-list="updateList"
    >
      <template #select-item="item">
        <img :src="getImg(item)" alt="User picture" class="user-picture" />
      </template>
    </BaseSearchField>

    <ProjectCalendar :is-range="true" class="date-picker" />

    <footer class="create-project__footer">
      <ButtonWithArrow
        :is-disabled="!projectName"
        class="button"
        @click="saveChanges"
      >
        <CustomText tag="span" text="Save Project" />
      </ButtonWithArrow>
    </footer>
  </div>
</template>

<script>
import {mapState, mapActions, createNamespacedHelpers} from 'vuex'
import {action} from '@store/constants'

import CustomText from '@/components/CustomText'
import BaseInput from '@/components/common/BaseInput'
import BaseSearchField from '@/components/BaseSearchField'
import AccountAnalysisSourcesTabs from '@/components/account-analysis/AccountAnalysisSourcesTabs'
import ButtonWithArrow from '@/components/common/ButtonWithArrow'
import ProjectCalendar from '@/components/datepicker/ProjectCalendar'

const {
  mapActions: mapAccountAnalysisActions,
  mapState: mapAccountAnalysisState,
} = createNamespacedHelpers('accountAnalysis')

export default {
  name: 'CreateAccountAnalysisProject',
  components: {
    BaseInput,
    AccountAnalysisSourcesTabs,
    ButtonWithArrow,
    BaseSearchField,
    CustomText,
    ProjectCalendar,
  },
  data() {
    return {
      projectName: '',
      newAccountProfile: '',
      pageNumber: 1,
    }
  },
  computed: {
    ...mapState({
      additionalFilters: (state) => state.additionalFilters,
      userInfo: (state) => state.userInfo,
      newWorkspace: (state) => state.newAccountAnalysisWorkspace,
      newProject: (state) => state.newAccountAnalysisProject,
    }),
    ...mapAccountAnalysisState({
      listOfProfilesHandle: (state) => state.listOfProfilesHandle,
      newProjectId: (state) => state.newProjectId,
      newWorkspaceId: (state) => state.newWorkspaceId,
    }),
    listOfProfiles() {
      return this.listOfProfilesHandle.list
    },
    accountProfile: {
      get() {
        return this.newAccountProfile
      },
      set(val) {
        this.newAccountProfile = val
        this.pageNumber = 1
        this.getProfiles(this.pageNumber)
      },
    },
    workspaceId() {
      return this.$route.params.workspaceId
    },
    profileNames() {
      return this.listOfProfiles.map((el) => el.user_alias)
    },
    defaultDateRange() {
      return [this.getLastWeeksDate(), new Date()]
    },
  },
  async created() {
    await this.getProfiles(this.pageNumber)

    if (this.defaultDateRange.length) {
      this[action.UPDATE_ADDITIONAL_FILTERS]({
        date_range: this.defaultDateRange,
      })
    }
  },
  methods: {
    ...mapActions([
      action.UPDATE_NEW_ACCOUNT_ANALYSIS_PROJECT,
      action.UPDATE_ADDITIONAL_FILTERS,
    ]),
    ...mapAccountAnalysisActions([
      action.GET_LIST_OF_PROFILE_HANDLE,
      action.CREATE_NEW_ACCOUNT_ANALYSIS_WORKSPACE,
      action.CREATE_NEW_ACCOUNT_ANALYSIS_PROJECT,
    ]),
    async getProfiles(pageNumber) {
      await this[action.GET_LIST_OF_PROFILE_HANDLE]({
        page_number: pageNumber,
        profile_per_page: 20,
        profiles_query: this.accountProfile,
      })
    },
    async updateList() {
      if (this.listOfProfilesHandle.profilesCount <= 20) return
      this.pageNumber = this.pageNumber + 1
      await this.getProfiles(this.pageNumber)
    },
    getLastWeeksDate() {
      const now = new Date()

      return new Date(now.getFullYear(), now.getMonth(), now.getDate() - 6)
    },
    async saveChanges() {
      await this[action.UPDATE_NEW_ACCOUNT_ANALYSIS_PROJECT]({
        title: this.projectName,
        profile_handle: this.accountProfile,
        source_filter: ['twitter'],
        members: [this.userInfo.id],
        creator: this.userInfo.id,
        start_search_date: this.additionalFilters.date_range[0],
        end_search_date: this.additionalFilters.date_range[1],
      })

      if (+this.workspaceId) {
        await this[action.CREATE_NEW_ACCOUNT_ANALYSIS_PROJECT]({
          ...this.newProject,
          workspace: +this.workspaceId,
        })
      } else {
        await this[action.CREATE_NEW_ACCOUNT_ANALYSIS_WORKSPACE]({
          ...this.newWorkspace,
          projects: [
            {
              ...this.newProject,
            },
          ],
        })
      }
      this.$router.push({
        name: 'AccountAnalysisDashboard',
        params: {
          projectId: this.newProjectId,
          workspaceId: this.newWorkspaceId || this.workspaceId,
        },
      })
    },
    selectProfile(name, searchValue) {
      this.accountProfile = searchValue
    },
    getImg(profileData) {
      return this.listOfProfiles.find(
        (profileOptions) => profileData.item === profileOptions.user_alias
      )?.user_picture
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

  .tabs {
    margin-bottom: 36px;
  }

  .input-name-field {
    max-width: 408px;
    margin-bottom: 32px;
  }

  .select-profile-handle {
    max-width: 408px;
    margin-bottom: 32px;

    .user-picture {
      width: 20px;
      height: 20px;
      margin-right: 10px;

      border-radius: 100%;
    }
  }

  .date-picker {
    max-width: 408px;
    margin-bottom: 72px;
  }

  .create-project__footer {
    display: flex;
    justify-content: flex-end;

    max-width: 408px;
  }
}
</style>
