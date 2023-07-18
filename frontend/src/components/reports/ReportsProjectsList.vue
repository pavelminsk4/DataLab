<template>
  <aside class="wrapper">
    <h4 class="wrapper__title">Projects list</h4>
    <div class="projects">
      <a
        v-for="project in projects"
        :key="project.id"
        :id="project.id"
        :class="['projects__item', currProjectId === project.id && 'active']"
        @click.stop="handleClick"
      >
        <BaseChips :chips-type="project.moduleType" />

        <div class="projects__title">{{ project.title }}</div>
      </a>
    </div>
  </aside>
</template>

<script>
import {mapState} from 'vuex'
import BaseChips from '@/components/BaseChips'

export default {
  name: 'ReportsProjectsList',
  components: {BaseChips},
  data() {
    return {
      currProjectId: null,
    }
  },
  computed: {
    ...mapState(['newReport']),
    projects() {
      return this.newReport.projects
    },
  },
  methods: {
    handleClick({currentTarget}) {
      const id = +currentTarget.id
      this.currProjectId = id
      const targetEl = document.getElementById(id)
      if (targetEl) {
        targetEl.scrollIntoView({behavior: 'smooth', alignToTop: true})
      }
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
      grid-template-columns: minmax(135px, 45%) 65%;
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

      @media (max-width: 1100px) {
        grid-template-columns: 57% 43%;
        gap: 5px;
      }

      .chips-height {
        height: 28px;
      }
    }

    &__title {
      width: 80%;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }
  }
}
</style>
