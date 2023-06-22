<template>
  <div class="story-report-wrapper scroll">
    <div class="item">
      <div class="title"><PostStoryReportIcon /> Post</div>
      <a
        class="summary link"
        :href="post.online_post.entry_links_href"
        target="_blank"
      >
        {{ post.online_post.feedlink__sourceurl }}
      </a>
    </div>

    <div class="item">
      <div class="title"><PencilIcon /> Summary</div>
      <div class="summary">
        <div>{{ post.header }}</div>
        <div class="summary-text">{{ post.text }}</div>
      </div>
    </div>

    <div class="item">
      <div class="title"><RelatedIcon />Related content</div>
      <a
        v-for="(item, index) in relatedLinks"
        :key="'link' + index"
        :href="item.link"
        target="_blank"
        class="summary link"
      >
        {{ item.linkName }}
      </a>
    </div>
  </div>

  <div v-if="isWhatsappFieldsShow" class="buttons">
    <BaseButton
      :is-disabled="true"
      :button-loading="buttonWhatsappLoading"
      @click="$emit('send-to-whatsapp', messageContent)"
    >
      Send to Whatsapp
    </BaseButton>
  </div>
</template>

<script>
import {createNamespacedHelpers} from 'vuex'
import BaseButton from '@/components/common/BaseButton'
import PostStoryReportIcon from '@/components/icons/PostStoryReportIcon'
import PencilIcon from '@/components/icons/PencilIcon'
import RelatedIcon from '@/components/icons/RelatedIcon'

const {mapState} = createNamespacedHelpers('twentyFourSeven')

const PUBLISHING = 'Publishing'

export default {
  name: 'TFSStoryReportTab',
  components: {
    BaseButton,
    PostStoryReportIcon,
    PencilIcon,
    RelatedIcon,
  },
  emits: ['send-to-whatsapp', 'change-original-content-language'],
  props: {
    post: {type: Object, required: true},
    buttonWhatsappLoading: {type: Boolean, required: true},
    translationLoading: {type: Boolean, required: true},
  },
  computed: {
    ...mapState(['statusMessage', 'items']),
    relatedLinks() {
      const linkedItems = this.items[this.post.status].results.find(
        (el) => el.id === this.post.id
      ).linked_items

      return linkedItems.map((element) => {
        return {
          link: element.online_post.entry_links_href,
          linkName: element.online_post.feedlink__sourceurl,
        }
      })
    },
    messageContent() {
      return `${this.post.online_post.feed_image_link} ${this.post.header} ${
        this.post.text
      } ${this.relatedLinks.join(' ')}`
    },
    isWhatsappFieldsShow() {
      return this.post.status === PUBLISHING
    },
  },
}
</script>

<style lang="scss" scoped>
.story-report-wrapper {
  display: flex;
  flex-direction: column;
  gap: 16px;

  height: 400px;

  .item {
    gap: 8px;

    .title {
      display: flex;
      align-items: center;
      gap: 12px;

      margin-bottom: 8px;

      font-weight: 600;
    }

    .summary {
      display: flex;
      flex-direction: column;
      gap: 8px;

      margin-left: 33px;
      .summary-text {
        font-size: 12px;
      }
    }

    .link {
      color: var(--link-color);
    }
  }
}
.buttons {
  display: flex;
  justify-content: flex-end;
  gap: 16px;

  margin: 36px -24px 0;
  padding: 18px 24px 0 0;

  border-top: 1px solid var(--border-color);
}
</style>
