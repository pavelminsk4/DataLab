<template>
  <aside class="wrapper">
    <h4 class="wrapper__title">Projects list</h4>
    <ul class="projects">
      <a
        v-for="project in projects"
        :key="project.id"
        :id="project.id"
        :href="'#' + project.id"
        :class="['projects__item', currProjectId === project.id && 'active']"
        @click.stop="handleClick"
      >
        <div class="chips-height">
          <BaseChips :chips-type="project.moduleType" />
        </div>
        <div>{{ project.title }}</div>
      </a>
    </ul>
  </aside>
</template>

<script>
import BaseChips from '@/components/BaseChips.vue'
export default {
  name: 'ReportsProjectsList',
  components: {BaseChips},
  data() {
    return {
      currProjectId: null,
    }
  },
  created() {
    this.projects = [
      {id: 120, title: 'المغرب', moduleType: 'Online'},
      {id: 89, title: 'a', moduleType: 'Online'},
      {id: 106, title: 'Dimension', moduleType: 'Online'},
      {id: 107, title: 'Argentina', moduleType: 'Online'},
      {id: 108, title: 'Alert', moduleType: 'Online'},
      {id: 109, title: 'Second Alert', moduleType: 'Online'},
      {id: 101, title: 'السعودية', moduleType: 'Online'},
      {id: 54, title: 'bel', moduleType: 'Online'},
      {id: 79, title: '1year', moduleType: 'Online'},
    ]
  },
  methods: {
    handleClick({currentTarget}) {
      this.currProjectId = +currentTarget.id
    },
  },
}
</script>

<style lang="scss" scoped>
.wrapper {
  width: 24vw;
  &__title {
    font-size: 16px;
    font-weight: 500;
  }

  .projects {
    display: grid;

    padding: 0;

    list-style: none;

    .active {
      background-color: var(--primary-active-color);
    }

    &__item {
      display: grid;
      grid-template-columns: 30% 70%;
      align-items: center;

      padding-left: 5px;
      height: 55px;

      box-shadow: 0 -1px 0 var(--border-color) inset;
      user-select: none;

      text-decoration: none;
      color: var(--typography-primary-color);

      &:hover {
        box-shadow: 0px 6px 18px rgba(113, 93, 231, 0.2);
      }
      .chips-height {
        height: 28px;
      }
    }
  }
}
</style>
