<template>
  <MainLayout>
    <div class="create-project-wrapper">
      <div>
        <h1 class="title">Dashboard</h1>
        <span class="hint">Keep all your projects in order by arranging them by topic</span>

        <div class="sort-wrapper">
          <span class="hint">Sort by</span>
          <div class="sort-option">Latest <SortIcon class="sort-icon" /></div>
        </div>
      </div>

      <div class="create-project-buttons">
        <BaseButton
            class="add-project-button"
            :is-not-background="true"
        >
          <PlusIcon class="add-workspace-button" />
          Add workspace
        </BaseButton>
        <BaseButton class="create-new-button">Create new project</BaseButton>
      </div>
    </div>
    <ProjectItem />
  </MainLayout>
</template>

<script>
import SortIcon from '@components/icons/SortIcon'
import PlusIcon from '@components/icons/PlusIcon'

import MainLayout from '@components/layout/MainLayout'
import ProjectItem from '@components/dashboard/ProjectItem'
import BaseButton from '@components/buttons/BaseButton'

export default {
  name: "DashboardList",
  components: {
    SortIcon,
    PlusIcon,
    BaseButton,
    MainLayout,
    ProjectItem,
  }
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

  .create-project-buttons {
    display: flex;
  }

  .add-project-button {
    display: flex;
    justify-content: center;
    align-items: center;

    width: 179px;

    margin-right: 10px;

    .add-workspace-button {
      margin-right: 12px;
    }
  }

  .create-new-button {
    width: 178px;
  }
</style>
