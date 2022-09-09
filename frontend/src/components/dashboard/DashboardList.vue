<template>
  <MainLayout>
    <div class="create-project-wrapper">
      <div>
        <h1 class="title">Dashboard</h1>
        <span class="hint"
          >Keep all your projects in order by arranging them by topic</span
        >

        <div class="sort-wrapper">
          <span class="hint">Sort by</span>
          <div class="sort-option">Latest <SortIcon class="sort-icon" /></div>
        </div>
      </div>

      <BaseButton class="create-new-button" @click="createWorkspace">
        Create new workspace
      </BaseButton>
    </div>
    <div class="items-wrapper">
      <ProjectItem
        v-for="(item, index) in workspaces"
        :key="index"
        :title="item.title"
        @click="navigateToWorkspace(item.id)"
      />
    </div>
  </MainLayout>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'

import SortIcon from '@components/icons/SortIcon'

import MainLayout from '@components/layout/MainLayout'
import ProjectItem from '@components/dashboard/ProjectItem'
import BaseButton from '@components/buttons/BaseButton'

export default {
  name: 'DashboardList',
  components: {
    SortIcon,
    BaseButton,
    MainLayout,
    ProjectItem,
  },
  computed: {
    ...mapGetters({
      workspaces: get.WORKSPACES,
      member: get.USER_ID,
    }),
  },
  async created() {
    await this[action.GET_WORKSPACES]()
    await this[action.GET_USER_INFORMATION]()
  },
  methods: {
    ...mapActions([
      action.GET_WORKSPACES,
      action.CREATE_WORKSPACE,
      action.GET_USER_INFORMATION,
    ]),
    createWorkspace() {
      this.loading = true
      this.$router.push({
        name: 'CreateProject',
      })
    },
    navigateToWorkspace(id) {
      this.loading = true
      this.$router.push({name: 'Workspace', params: {workspaceId: id}})
    },
  },
}
</script>

<style lang="scss" scoped>
.title {
  margin: 0 0 8px;

  color: var(--primary-text-color);

  font-style: normal;
  font-weight: 600;
  font-size: 36px;
  line-height: 42px;
}

.hint {
  color: var(--secondary-text-color);

  font-style: normal;
  font-weight: 400;
  font-size: 14px;
  line-height: 20px;
}

.create-project-wrapper {
  display: flex;
  justify-content: space-between;
}

.sort-wrapper {
  display: flex;

  margin: 34px 0 22px;

  color: var(--primary-text-color);

  font-style: normal;
  font-weight: 400;
  font-size: 14px;
  line-height: 20px;
}

.sort-option {
  display: flex;
  align-items: center;

  margin-left: 15px;
}

.sort-icon {
  margin-left: 7px;
}

.create-new-button {
  width: 178px;
}

.items-wrapper {
  display: flex;
  flex-wrap: wrap;

  margin: 0 -24px 0;
}
</style>
