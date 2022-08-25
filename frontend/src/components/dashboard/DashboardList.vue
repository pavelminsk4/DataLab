<template>
  <MainLayout>
    <h1 class="title">Dashboard</h1>
    <span class="hint">Keep all your projects in order by arranging them by topic</span>

    <div class="sort-wrapper">
      <span class="hint">Sort by</span>
      <div class="sort-option">Latest <SortIcon class="sort-icon" /></div>
    </div>

    <ProjectItem />
  </MainLayout>
</template>

<script>
import MainLayout from "@/components/layout/MainLayout";
import ProjectItem from "@/components/dashboard/ProjectItem";

import SortIcon from '../icons/SortIcon'

export default {
  name: "DashboardList",
  components: {
    MainLayout,
    SortIcon,
    ProjectItem
  }
}
</script>

<style scoped>
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
</style>
