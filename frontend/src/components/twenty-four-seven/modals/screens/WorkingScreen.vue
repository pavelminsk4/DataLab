<template>
  <div class="working-wrapper">
    <section class="view-content-wrapper">
      <TFSPostCard
        :postDetails="post.online_post"
        :is-back="post.is_back"
        :card-status="post.status"
        :item-id="post.id"
        class="post-card"
      />

      <div class="related-content">
        <div class="title-wrapper">
          <span class="title">Related content</span>
          <span class="results">{{ relatedContent.length }} results</span>
        </div>

        <TFSPostCard
          v-for="(item, index) in relatedContent"
          :key="'related' + index"
          :postDetails="item.online_post"
          :is-back="item.is_back"
          :card-status="item.status"
          :item-id="item.id"
          :is-related-content="true"
          class="post-related-content"
        />
      </div>
    </section>
    <section class="working-content-wrapper">
      <div class="panel-tabs">
        <span
          v-for="(item, index) in panelTabs"
          :key="item + index"
          :class="['tab', item === activeTab && 'active-tab']"
        >
          {{ item }}
        </span>
      </div>

      <div class="post-title">
        {{ post.online_post.entry_title }}
      </div>
      <div class="post-description">
        {{ post.online_post.entry_summary }}
      </div>
    </section>
  </div>
</template>

<script>
import {createNamespacedHelpers} from 'vuex'
import {action} from '@store/constants'

import TFSPostCard from '@/components/TFSPostCard'

const {mapState, mapActions} = createNamespacedHelpers('twentyFourSeven')

export default {
  name: 'WorkingScreen',
  components: {TFSPostCard},
  props: {
    post: {type: Object, required: true},
  },
  data() {
    return {
      panelTabs: ['Original content', 'Summary', 'Q&A Check', 'Story report'],
    }
  },
  computed: {
    ...mapState(['items', 'relatedContent']),
    activeTab() {
      return this.$route.query.tab
    },
  },
  created() {
    this[action.GET_TFS_RELATED_CONTENT](this.post.id)
  },
  methods: {
    ...mapActions([action.GET_TFS_RELATED_CONTENT]),
  },
}
</script>

<style lang="scss" scoped>
.working-wrapper {
  display: flex;

  width: 100%;

  .view-content-wrapper {
    width: 50%;
    padding-right: 14px;

    .post-card {
      width: 100%;
    }

    .related-content {
      display: flex;
      flex-direction: column;

      margin-top: 40px;

      .title-wrapper {
        display: flex;
        align-items: center;
        gap: 12px;

        margin-bottom: 28px;

        .title {
          font-style: normal;
          font-weight: 600;
          font-size: 20px;
          color: var(--typography-primary-color);
        }

        .results {
          font-style: normal;
          font-weight: 600;
          font-size: 14px;
          color: var(--typography-secondary-color);
        }
      }

      .post-related-content {
        width: 100%;
        margin-bottom: 20px;

        background: var(--primary-active-color);
      }
    }
  }

  .working-content-wrapper {
    width: 50%;
    padding: 24px;
    margin: -24px -24px -24px 24px;

    background-color: var(--background-primary-color);
    .panel-tabs {
      display: flex;
      flex-wrap: nowrap;
      justify-content: space-between;

      .tab {
        position: relative;

        padding: 4px 18px;

        background: var(--background-additional-color);
        border-radius: 10px;

        cursor: pointer;

        font-style: normal;
        font-weight: 400;
        font-size: 14px;
        line-height: 20px;

        &:not(:last-child):after {
          content: '';
          position: absolute;
          top: 50%;
          right: -8.5px;
          transform: translateY(-50%);

          width: 4px;
          height: 4px;
          border-radius: 100px;
          background-color: var(--icon-primary-color);
        }
      }

      .active-tab {
        color: var(--button-text-color);
        background-color: var(--button-primary-color);
      }
    }

    .post-title {
      margin: 22px 0 16px;

      font-style: normal;
      font-weight: 600;
      font-size: 20px;
      line-height: 28px;
      color: var(--typography-title-color);
    }

    .post-description {
      font-style: normal;
      font-weight: 400;
      font-size: 14px;
      line-height: 20px;
      color: var(--typography-primary-color);
    }
  }
}
</style>
