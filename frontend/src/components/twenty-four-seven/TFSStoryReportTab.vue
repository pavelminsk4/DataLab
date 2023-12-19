<template>
  <div class="story-report-wrapper scroll">
    <div class="item">
      <div class="title"><PostStoryReportIcon /><CustomText text="Post" /></div>
      <div class="post-title">
        {{ post.post.entry_title }}
      </div>
    </div>

    <div class="item">
      <div class="title"><PencilIcon /><CustomText text="Summary" /></div>
      <div class="summary">
        <div>{{ post.header }}</div>
        <div class="summary-text">{{ post.text }}</div>
      </div>
    </div>

    <a class="summary link" :href="post.post.entry_links_href" target="_blank">
      {{ post.post.feedlink__sourceurl }}
    </a>

    <div class="item">
      <div class="title">
        <RelatedIcon /> <CustomText text="Related content" />
      </div>
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
    <MultiSelect
      v-model="selectedPhoneNumbers"
      :options="recipientsNames"
      item-name="number"
      template-title="Phone numbers"
      select-name="phone-numbers"
      class="phone-numbers-select"
    />
    <div class="whatsapp-button">
      <BaseButton
        :button-loading="buttonWhatsappLoading"
        @click="$emit('send-to-whatsapp', whatsappNumbers, messageContent)"
      >
        <CustomText text="Send to Whatsapp" />
      </BaseButton>
      <div v-if="statusMessage" class="error-message">
        <ErrorIcon class="error-icon" />
        <CustomText :text="statusMessage" />
      </div>
    </div>
  </div>
</template>

<script>
import {createNamespacedHelpers} from 'vuex'

import CustomText from '@components/CustomText'
import BaseButton from '@components/common/BaseButton'
import PostStoryReportIcon from '@components/icons/PostStoryReportIcon'
import PencilIcon from '@components/icons/PencilIcon'
import RelatedIcon from '@components/icons/RelatedIcon'
import MultiSelect from '@components/MultiSelect'
import ErrorIcon from '@components/icons/ErrorIcon'

const {mapState} = createNamespacedHelpers('twentyFourSeven')

const PUBLISHING = 'Publishing'

export default {
  name: 'TFSStoryReportTab',
  components: {
    BaseButton,
    PostStoryReportIcon,
    PencilIcon,
    RelatedIcon,
    MultiSelect,
    ErrorIcon,
    CustomText,
  },
  emits: [
    'send-to-whatsapp',
    'change-original-content-language',
    'update:selectedNumbers',
  ],
  props: {
    post: {type: Object, required: true},
    buttonWhatsappLoading: {type: Boolean, required: true},
    translationLoading: {type: Boolean, required: true},
    phoneNumbers: {type: Array, default: () => []},
  },
  data() {
    return {
      selectedNumbers: null,
    }
  },
  computed: {
    ...mapState(['statusMessage', 'items']),
    relatedLinks() {
      const linkedItems = this.items[this.post.status].results.find(
        (el) => el.id === this.post.id
      ).linked_items

      return linkedItems.map((element) => {
        return {
          link: element.post.entry_links_href,
          linkName: element.post.feedlink__sourceurl,
        }
      })
    },
    messageContent() {
      return `${this.post.post.feedlink__sourceurl} ${this.post?.header} ${
        this.post?.text
      } ${this.relatedLinks.map((link) => link.link).join(' ')}`
    },
    isWhatsappFieldsShow() {
      return this.post.status === PUBLISHING
    },
    recipientsNames() {
      return this.phoneNumbers.map((recipient) => {
        return {title: recipient.name, id: recipient.mobile_number}
      })
    },
    selectedPhoneNumbers: {
      get() {
        return this.selectedNumbers || this.recipientsNames
      },
      set(selectedValue) {
        this.selectedNumbers = selectedValue
        this.$emit('update:selectedNumbers', selectedValue)
      },
    },
    whatsappNumbers() {
      return this.selectedPhoneNumbers.map((recipient) =>
        recipient.id.replace(/[^0-9]/g, '')
      )
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

    .post-title {
      margin-left: 33px;
    }

    .link {
      color: var(--link-color);
    }
  }
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
.buttons {
  display: flex;
  justify-content: flex-end;
  align-items: center;
  gap: 16px;

  margin: 36px -24px 0;
  padding: 18px 24px 0 0;

  border-top: 1px solid var(--border-color);

  .phone-numbers-select {
    width: 200px;
    height: 40px;
  }

  .whatsapp-button {
    position: relative;

    .error-message {
      position: absolute;

      display: flex;
      align-items: center;
      gap: 4px;

      font-size: 12px;
      color: var(--error-primary-color);

      .error-icon {
        width: 12px;
        height: 12px;

        color: var(--error-primary-color);
      }
    }
  }
}
</style>
