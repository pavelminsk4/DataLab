<template>
  <div v-if="itemsTest" class="drag-n-drop-wrapper">
    <div
      v-for="(item, index) in statuses"
      :key="'status' + index"
      :id="'zone-' + index"
      class="drop-zone"
      @drop="onDrop($event, index)"
      @dragenter.prevent
      @dragover.prevent
      @mousedown="getIdArea(index)"
    >
      <div class="drop-section">
        {{ item.status }}
        <div class="results">1000</div>
      </div>

      <div
        v-for="item1 in getList(item.status)"
        :key="item1.id"
        class="drag-el"
        draggable="true"
        @dragstart="startDrag($event, item1)"
      >
        <TFSPostCard
          :postDetails="item1.online_post"
          :cardStatus="item1.status"
          :itemId="item1.id"
          class="post-card"
          @change-status="changeStatus"
        />
      </div>
    </div>
  </div>
</template>

<script>
import TFSPostCard from '@/components/TFSPostCard'

export default {
  name: 'TFSDragAndDrop',
  components: {TFSPostCard},
  props: {
    itemsTest: {type: Object, reqared: true},
  },
  data() {
    return {
      currentAreaId: null,
      statuses: [
        {status: 'Picking', list: 1, items: []},
        {status: 'Summary', list: 2, items: []},
        {status: 'Q&A Check', list: 3, items: []},
        {status: 'Publishing', list: 4, items: []},
        {status: 'Published', list: 5, items: []},
      ],
    }
  },
  methods: {
    getList(status) {
      return this.itemsTest[status]
    },

    startDrag($event, item) {
      $event.dataTransfer.dropEffect = 'move'
      $event.dataTransfer.effectAllowed = 'move'
      $event.dataTransfer.setData('itemID', item.id)
    },

    async onDrop($event, index) {
      const itemID = $event.dataTransfer.getData('itemID')
      console.log(itemID)
      await this.$emit(
        'update-status',
        itemID,
        this.statuses[index].status,
        this.statuses[this.currentAreaId].status
      )
    },

    getIdArea(id) {
      this.currentAreaId = id
    },

    changeStatus(itemId, newStatus, oldStatus) {
      this.$emit('change-status-via-dropdown', itemId, newStatus, oldStatus)
    },
  },
}
</script>

<style lang="scss" scoped>
.drag-n-drop-wrapper {
  display: flex;

  .drop-zone {
    width: 320px;
    flex-shrink: 0;
    .drop-section {
      display: flex;
      gap: 4px;

      padding: 12px 20px;
      margin-bottom: 24px;

      border-top: 3px solid var(--neutral-primary-color);
      border-radius: 8px;
      background-color: var(--background-secondary-color);

      font-style: normal;
      font-weight: 500;
      font-size: 16px;
      line-height: 20px;
      color: var(--typography-title-color);

      .results {
        padding: 2px 5px;

        border-radius: 14px;
        background-color: var(--icon-primary-color);

        text-align: center;
        font-size: 14px;
        color: var(--button-text-color);
      }
    }
  }
}

.drop-zone {
  width: 50%;
  margin: 50px auto;
  padding: 10px;
  min-height: 10px;
}

.drag-el {
  color: azure;
  padding: 5px;
  margin-bottom: 10px;

  .post-card {
    width: 290px;
  }
}

.drag-el:nth-last-of-type(1) {
  margin-bottom: 0;
}
</style>
