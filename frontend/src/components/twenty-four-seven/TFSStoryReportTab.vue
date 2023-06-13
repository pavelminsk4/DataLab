<template>
  <div class="story-report-wrapper">
    <div class="item">
      <div class="title"><PostStoryReportIcon /> Post</div>
      <a
        class="summary link"
        :href="post.online_post.entry_links_href"
        target="_blank"
      >
        {{ post.online_post.entry_links_href }}
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
        :href="item"
        target="_blank"
        class="summary link"
      >
        {{ item }}
      </a>
    </div>
  </div>

  <div class="buttons">
    <BaseInput
      v-model="phoneNumber"
      :hasError="isMessageSent"
      :error-message="statusMessage"
      label=" "
      type="tel"
      placeholder="+** *** *** ***"
      class="phone-input"
    />
    <BaseButton
      :button-loading="buttonWhatsappLoading"
      @click="$emit('send-to-whatsapp', phoneNumber, messageContent)"
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
import BaseInput from '@/components/common/BaseInput'

const {mapState} = createNamespacedHelpers('twentyFourSeven')

export default {
  name: 'TFSStoryReportTab',
  components: {
    BaseButton,
    PostStoryReportIcon,
    PencilIcon,
    RelatedIcon,
    BaseInput,
  },
  emits: ['send-to-whatsapp', 'change-original-content-language'],
  props: {
    post: {type: Object, required: true},
    buttonWhatsappLoading: {type: Boolean, required: true},
  },
  data() {
    return {
      phoneNumber: '',
    }
  },
  computed: {
    ...mapState(['relatedContent', 'statusMessage']),
    relatedLinks() {
      return this.relatedContent.map(
        (element) => element.online_post.entry_links_href
      )
    },
    messageContent() {
      return `${this.post.online_post.feed_image_link} ${this.post.header} ${
        this.post.text
      } ${this.relatedLinks.join(' ')}`
    },
    isMessageSent() {
      return this.statusMessage === 'Message not sent'
    },
  },
}
</script>

<style lang="scss" scoped>
.story-report-wrapper {
  display: flex;
  flex-direction: column;
  gap: 16px;

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

  .phone-input {
    margin-top: -4px;
  }
}
</style>
